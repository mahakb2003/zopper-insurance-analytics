# 📊 Insurance Portfolio Risk & Profitability Analytics

An end-to-end data analytics project analyzing insurance portfolio profitability, claim exposure, and risk distribution using Python, Pandas, and Power BI.

This project simulates a real-world insurance analytics scenario where an insurer evaluates policy performance, claim behavior, and financial risk to improve pricing strategy and portfolio profitability.

## 📊 Power BI Dashboard
<p align="center"> <img src="images/insurance_dashboard.png" width="700"> </p>

The interactive dashboard tracks key insurance KPIs including:

-Total Premium Revenue
-Total Claim Cost
-Loss Ratio
-Claim Frequency
-Claim Trends by Month
-Risk Exposure by Policy Tenure

## 🧠 Business Context

Insurance companies must constantly evaluate the financial performance of their policy portfolios.
A key metric used in the industry is the Loss Ratio, defined as:

Loss Ratio = Total Claims / Total Premium

A high loss ratio indicates that claim payouts exceed premium revenue, which can lead to financial losses for the insurer.
However, analyzing large insurance datasets across policies and claims can be challenging.
This project builds a data-driven insurance analytics framework that helps insurers understand claim patterns, evaluate profitability, and identify risk factors in their portfolio.

## 🎯 Business Impact

The analysis revealed several important insights about the simulated insurance portfolio.

1. Portfolio Loss Ratio

-The overall portfolio shows a loss ratio of approximately 2.05, meaning total claims are more than double the premium revenue collected.
-This indicates that the simulated insurance portfolio is currently unprofitable.

2. Claim Frequency

-Only 4.9% of vehicles have filed claims, while 95.1% remain potential claims.
-This suggests that the insurer still carries significant future claim liability during the remaining policy tenure.

3. Policy Tenure Profitability

Policy tenure significantly affects portfolio profitability.
The analysis shows:

-3-year policies are the most profitable
-1-year policies show the highest loss ratio
-4-year policies carry high claim exposure

## 🛠 Tech Stack
-Data Simulation
-Python
-NumPy
-Data Processing
-Python
-Pandas

Data Analysis
-Jupyter Notebook

Data Visualization
-Power BI
-Matplotlib

Development Environment
-VS Code
-Git
-GitHub

## ⚙️ Data Pipeline & Workflow
Data Simulation

A Python pipeline was built to simulate large-scale insurance datasets.

Scripts used:

1.policy_sales_generation.py
2.claims_data_generation.py
3.prepare_insurance_dataset.py

The pipeline:

-Generates policy sales data
-Simulates insurance claims using business rules
-Cleans and integrates datasets
-Exports the final analytical dataset

## Dataset Creation

Two main datasets were generated:

1️⃣ Policy Sales Dataset
Represents vehicle insurance policies purchased during 2024.
Key characteristics:
-1,000,000 policies simulated
-Each record represents a unique vehicle and customer
-Vehicle value assumed: ₹100,000
-Policy Tenure Distribution
Tenure	Distribution
1 Year	20%
2 Years	30%
3 Years	40%
4 Years	10%
Premium Calculation Rule
Premium = Policy_Tenure × 100

2️⃣ Claims Dataset
-Simulates insurance claims filed against policies based on predefined rules.
-Dataset fields include:
-Claim_ID
-Customer_ID
-Vehicle_ID
-Claim_Amount
-Claim_Date
-Claim_Type
-Claim Amount Rule
-Claim Amount = 10% of Vehicle Value
-Claim Simulation Rules

Claims were generated according to business logic:

For 2025

Vehicles purchased on the 7th, 14th, 21st, and 28th of each month were eligible for claims

30% of these vehicles filed a claim

For 2026

Additional claims generated between Jan 1 – Feb 28

10% of vehicles with 4-year tenure filed claims

Vehicles with a previous claim could file a second claim
