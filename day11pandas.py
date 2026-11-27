# ============================
# Day 11 — Reading CSV with Pandas
# ============================

import pandas as pd

# 1. Read the CSV file into a DataFrame
# Make sure 'data12.csv' is in the same folder as this script!
df = pd.read_csv("data12.csv")

# 2. Print the whole table
print("--- Full Table ---")
print(df)

# 3. Print just the 'Name' column
print("\n--- Names Column ---")
print(df["Name"])

# 4. Do math on a column
print("\n--- Age Math ---")
print("Average Age:", df["Age"].mean())
print("Highest Age:", df["Age"].max())
