# ============================
# Day 12 — Filtering Data
# ============================

import pandas as pd

# 1. Create the dataset
data = [
    {"Name": "Rohan", "Age": 24, "City": "Delhi", "Sales": 50000},
    {"Name": "Priya", "Age": 22, "City": "Mumbai", "Sales": 65000},
    {"Name": "Amit", "Age": 27, "City": "Delhi", "Sales": 45000},
    {"Name": "Neha", "Age": 25, "City": "Bangalore", "Sales": 80000}
]

df = pd.DataFrame(data)

# 2. Print the whole table
print("--- Full Table ---")
print(df)

# 3. Filter: Only people from Delhi
print("\n--- People from Delhi ---")
delhi_people = df[df["City"] == "Delhi"]
print(delhi_people)

# 4. Filter: Only people with Sales greater than 50000
print("\n--- High Sales (Above 50k) ---")
high_sales = df[df["Sales"] > 50000]
print(high_sales)

# 5. Multiple Conditions (AND) - City is Delhi AND Sales > 45k
# Note: Use & for AND, and wrap each condition in parentheses ()
print("\n--- Delhi + High Sales ---")
delhi_high = df[(df["City"] == "Delhi") & (df["Sales"] > 45000)]
print(delhi_high)