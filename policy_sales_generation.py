import pandas as pd
import numpy as np
from pathlib import Path

# ----------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------

TOTAL_POLICIES = 1_000_000
BASE_VEHICLE_VALUE = 100000

TENURE_PROBABILITY = {
    1: 0.20,
    2: 0.30,
    3: 0.40,
    4: 0.10
}

np.random.seed(42)


# ----------------------------------------------------
# GENERATE POLICY TENURE BASED ON DISTRIBUTION
# ----------------------------------------------------

def generate_policy_tenure(size):
    tenure_values = list(TENURE_PROBABILITY.keys())
    probabilities = list(TENURE_PROBABILITY.values())
    return np.random.choice(tenure_values, size=size, p=probabilities)


# ----------------------------------------------------
# GENERATE PURCHASE DATES EVENLY ACROSS 2024
# ----------------------------------------------------

def generate_purchase_dates(size):

    dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")

    repeated_dates = np.repeat(
        dates.values, 
        repeats=int(np.ceil(size / len(dates)))
    )[:size]

    np.random.shuffle(repeated_dates)

    return pd.to_datetime(repeated_dates)


# ----------------------------------------------------
# BUILD POLICY DATASET
# ----------------------------------------------------

def create_policy_dataset(n):

    customer_id = np.arange(1, n + 1)
    vehicle_id = np.arange(500001, 500001 + n)

    tenure = generate_policy_tenure(n)

    purchase_dates = generate_purchase_dates(n)

    start_dates = purchase_dates + pd.Timedelta(days=365)

    end_dates = start_dates + pd.to_timedelta(tenure * 365, unit="D")

    premium = tenure * 100

    vehicle_value = np.full(n, BASE_VEHICLE_VALUE)

    df = pd.DataFrame({
        "Customer_ID": customer_id,
        "Vehicle_ID": vehicle_id,
        "Vehicle_Value": vehicle_value,
        "Premium": premium,
        "Policy_Purchase_Date": purchase_dates,
        "Policy_Start_Date": start_dates,
        "Policy_End_Date": end_dates,
        "Policy_Tenure": tenure
    })

    return df


# ----------------------------------------------------
# GENERATE DATA
# ----------------------------------------------------

policy_sales = create_policy_dataset(TOTAL_POLICIES)


# ----------------------------------------------------
# SAVE DATASET
# ----------------------------------------------------

from pathlib import Path

# ----------------------------------------------------
# SAVE DATASET
# ----------------------------------------------------

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)   # creates folder if it doesn't exist

output_file = data_folder / "policy_sales_data.csv"

policy_sales.to_csv(output_file, index=False)


# ----------------------------------------------------
# QUICK VALIDATION
# ----------------------------------------------------

print("Dataset Shape:", policy_sales.shape)
print("\nTenure Distribution:")
print(policy_sales["Policy_Tenure"].value_counts(normalize=True))

print("\nPurchase Date Range:")
print(policy_sales["Policy_Purchase_Date"].min())
print(policy_sales["Policy_Purchase_Date"].max())