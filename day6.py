# ============================
# Day 6 — Strings & Text Cleaning
# ============================

# 1. Basic String Methods
name1 = "  rohan  "
name2 = "PRIYA"
name3 = "amit kumar"

print("--- Basic Cleaning ---")
print(name1.strip())       # Removes spaces from edges
print(name2.title())       # Capitalizes first letter
print(name3.title())       # Capitalizes every word

# 2. Splitting strings
sentence = "Data Analysis is fun"
words = sentence.split(" ")
print("\n--- Split ---")
print(words)

# 3. Applying cleaning to a whole List (List Comprehension)
cities = ["  delhi ", "MUMBAI", " bangalore", "Chennai  "]
clean_cities = [c.strip().title() for c in cities]
print("\n--- Cleaned Cities ---")
print(clean_cities)

# 4. Real-world Example: Clean a column in a DataFrame
import pandas as pd

data = {
    "Name": ["  rohan ", "PRIYA", "amit kumar"],
    "City": [" delhi", "MUMBAI ", "bangalore "]
}

df = pd.DataFrame(data)
print("\n--- Messy DataFrame ---")
print(df)

# We use .str to apply string methods to a whole Pandas column!
df["Name"] = df["Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

print("\n--- Clean DataFrame ---")
print(df)