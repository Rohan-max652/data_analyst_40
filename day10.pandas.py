# ============================
# Day 10 — Introduction to Pandas
# ============================

import pandas as pd

# 1. Creating a DataFrame from a List of Dictionaries
data = [
    {"Name": "Rohan", "Age": 24, "City": "Delhi"},
    {"Name": "Priya", "Age": 22, "City": "Mumbai"},
    {"Name": "Amit", "Age": 27, "City": "Bangalore"}
]

df = pd.DataFrame(data)

print("--- The DataFrame Table ---")
print(df)

# 2. Getting basic info about the table
print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- First 2 Rows (head) ---")
print(df.head(2))

# 3. Selecting a single column
print("\n--- Just the Names Column ---")
print(df["Name"])

# 4. Doing Math on a column (No loops needed!)
print("\n--- Math on the Age Column ---")
print("Average Age:", df["Age"].mean())
print("Max Age:", df["Age"].max())
print("Min Age:", df["Age"].min())