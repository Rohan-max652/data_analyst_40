# ============================
# Day 4 — Dictionaries
# ============================

# 1. Create a dictionary
person = {
    "name": "Rohan", 
    "age": 24, 
    "city": "Delhi", 
    "salary": 45000
}

print("--- Basic Dictionary ---")
print(person["name"])
print(person["age"])

# 2. Modify and Add
person["designation"] = "Analyst"  # Add new key
person["salary"] = 50000           # Update existing key
print("\n--- Updated Dictionary ---")
print(person)

# 3. Dictionary Methods
print("\n--- Methods ---")
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# 4. Revenue Dictionary
revenue = {"Jan": 125000, "Feb": 148000, "Mar": 132500, "Apr": 175000}

print("\n--- Revenue Data ---")
# Total revenue
total = sum(revenue.values())
print("Total Revenue:", total)

# Average revenue
average = total / len(revenue)
print("Average Revenue:", average)

# Highest revenue month
best_month = max(revenue, key=revenue.get)
print(f"Highest Revenue: {best_month} (₹{revenue[best_month]:,})")

# Lowest revenue month
worst_month = min(revenue, key=revenue.get)
print(f"Lowest Revenue: {worst_month} (₹{revenue[worst_month]:,})")

# 5. Looping through a dictionary
print("\n--- Formatted Loop ---")
for month, amount in revenue.items():
    print(f"{month}: ₹{amount:,}")