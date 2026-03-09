import pandas as pd

# ----------------------------------------------------
# 1. LOAD DATA
# ----------------------------------------------------

policies = pd.read_csv("data/policy_sales_data.csv")
claims = pd.read_csv("data/claims_data.csv")

print("Datasets loaded successfully")


# ----------------------------------------------------
# 2. MERGE DATASETS
# ----------------------------------------------------

df = policies.merge(
    claims,
    how="left",
    on="Vehicle_ID"
)

print("Datasets merged successfully")


# ----------------------------------------------------
# 3. HANDLE DUPLICATE CUSTOMER COLUMNS
# ----------------------------------------------------

if "Customer_ID_x" in df.columns:
    df = df.drop(columns=["Customer_ID_y"])
    df = df.rename(columns={"Customer_ID_x": "Customer_ID"})


# ----------------------------------------------------
# 4. HANDLE MISSING VALUES
# ----------------------------------------------------

# vehicles without claims → claim amount = 0
df["Claim_Amount"] = df["Claim_Amount"].fillna(0)


# ----------------------------------------------------
# 5. CONVERT DATE COLUMNS
# ----------------------------------------------------

date_cols = [
    "Policy_Purchase_Date",
    "Policy_Start_Date",
    "Policy_End_Date",
    "Claim_Date"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col])


# ----------------------------------------------------
# 6. CREATE DERIVED COLUMNS
# ----------------------------------------------------

# Claim indicator
df["Claim_or_Not"] = df["Claim_ID"].notna().astype(int)

# Purchase month
df["Purchase_Month"] = df["Policy_Purchase_Date"].dt.month

# Claim year
df["Claim_Year"] = df["Claim_Date"].dt.year

# Claim month
df["Claim_Month"] = df["Claim_Date"].dt.month

# Policy tenure in days
df["Tenure_Days"] = df["Policy_Tenure"] * 365


# ----------------------------------------------------
# 7. DATA TYPE CLEANING
# ----------------------------------------------------

df["Claim_Type"] = df["Claim_Type"].astype("Int64")
df["Claim_Year"] = df["Claim_Year"].astype("Int64")
df["Claim_Month"] = df["Claim_Month"].astype("Int64")

# ----------------------------------------------------
# 8. DATA VALIDATION CHECKS
# ----------------------------------------------------

print("\n==============================")
print("DATA VALIDATION CHECKS")
print("==============================")

# Dataset shape
print("\nDataset Shape:", df.shape)

# Duplicate vehicle check
print("\nDuplicate Vehicle IDs:", df["Vehicle_ID"].duplicated().sum())


# ----------------------------------------------------
# 9. CLAIM DISTRIBUTION VALIDATION
# ----------------------------------------------------

print("\nClaim Distribution Validation:")

claim_distribution = df.groupby("Vehicle_ID")["Claim_ID"].count().value_counts()
print(claim_distribution)

print("""
Interpretation:
- Majority of vehicles filed no claims
- Some vehicles filed one claim
- A small number of vehicles filed two claims

This pattern aligns with the assignment rules where vehicles may file
a second claim in 2026.
""")


# ----------------------------------------------------
# 10. DATE RANGE VALIDATION
# ----------------------------------------------------

print("\nDate Range Validation:")

purchase_range = (df["Policy_Purchase_Date"].min(), df["Policy_Purchase_Date"].max())
start_range = (df["Policy_Start_Date"].min(), df["Policy_Start_Date"].max())
claim_range = (df["Claim_Date"].min(), df["Claim_Date"].max())

print("\nPolicy Purchase Date Range:", purchase_range)
print("Policy Start Date Range:", start_range)
print("Claim Date Range:", claim_range)

print("""
Expected Date Ranges:
Policy Purchase : January 1, 2024 – December 31, 2024
Policy Start    : January 1, 2025 – December 31, 2025
Claims          : 2025 and early 2026
""")


# ----------------------------------------------------
# 11. SAVE FINAL CLEANED DATASET
# ----------------------------------------------------

df.to_csv("data/cleaned_insurance_analytics.csv", index=False)

print("\nCleaned dataset saved successfully.")
print("Location: data/cleaned_insurance_analytics.csv")