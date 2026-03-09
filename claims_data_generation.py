import pandas as pd
import numpy as np

np.random.seed(84)

# -------------------------
# LOAD POLICY DATA
# -------------------------

policies = pd.read_csv("data/policy_sales_data.csv")

policies["Policy_Start_Date"] = pd.to_datetime(policies["Policy_Start_Date"])
policies["Policy_End_Date"] = pd.to_datetime(policies["Policy_End_Date"])
policies["Policy_Purchase_Date"] = pd.to_datetime(policies["Policy_Purchase_Date"])

claims = []
claim_id = 1

# -------------------------
# CLAIMS FOR 2025
# -------------------------

eligible_days = [7, 14, 21, 28]

eligible_2025 = policies[
    policies["Policy_Purchase_Date"].dt.day.isin(eligible_days)
]

claims_2025 = eligible_2025.sample(frac=0.30, random_state=42)

claimed_vehicles_2025 = set()

for _, row in claims_2025.iterrows():

    claim_date = row["Policy_Start_Date"]

    if row["Policy_Start_Date"] <= claim_date <= row["Policy_End_Date"]:

        claims.append({
            "Claim_ID": claim_id,
            "Customer_ID": row["Customer_ID"],
            "Vehicle_ID": row["Vehicle_ID"],
            "Claim_Amount": row["Vehicle_Value"] * 0.10,
            "Claim_Date": claim_date,
            "Claim_Type": 1
        })

        claimed_vehicles_2025.add(row["Vehicle_ID"])

        claim_id += 1


# -------------------------
# CLAIMS FOR 2026
# -------------------------

four_year_policies = policies[policies["Policy_Tenure"] == 4]

claim_period_start = pd.Timestamp("2026-01-01")
claim_period_end = pd.Timestamp("2026-02-28")

active_four_year = four_year_policies[
    (four_year_policies["Policy_Start_Date"] <= claim_period_end) &
    (four_year_policies["Policy_End_Date"] >= claim_period_start)
]

claims_2026 = active_four_year.sample(frac=0.10, random_state=42)

date_range = pd.date_range("2026-01-01", "2026-02-28")

for i, (_, row) in enumerate(claims_2026.iterrows()):

    claim_date = date_range[i % len(date_range)]

    if row["Policy_Start_Date"] <= claim_date <= row["Policy_End_Date"]:

        claim_type = 2 if row["Vehicle_ID"] in claimed_vehicles_2025 else 1

        claims.append({
            "Claim_ID": claim_id,
            "Customer_ID": row["Customer_ID"],
            "Vehicle_ID": row["Vehicle_ID"],
            "Claim_Amount": row["Vehicle_Value"] * 0.10,
            "Claim_Date": claim_date,
            "Claim_Type": claim_type
        })

        claim_id += 1


# -------------------------
# CREATE DATAFRAME
# -------------------------

claims_df = pd.DataFrame(claims)

# -------------------------
# SAVE CSV
# -------------------------

claims_df.to_csv("data/claims_data.csv", index=False)

print("Claims data generated successfully")
print("Total Claims:", len(claims_df))