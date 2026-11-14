# ============================
# Day 2 — Lists & Slicing
# ============================

# 1. Creating a list
months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [12000, 15500, 9800, 17200, 14300]

# 2. Indexing and Slicing
print("First month:", months[0])
print("First 3 months:", months[:3])
print("Reversed:", months[::-1])

# 3. Modifying lists
months.append("Jun")
revenue.insert(1, 10000)
months.remove("Mar")
revenue.pop()

# 4. Aggregations
print("Total Revenue:", sum(revenue))
print("Average Revenue:", sum(revenue) / len(revenue))

# 5. Looping with enumerate
for i, s in enumerate(revenue, start=1):
    print(f"Day {i}: ₹{s:,}")