# ============================
# Day 5 — List Comprehensions
# ============================

# 1. Filter numbers greater than 5
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_5 = [n for n in nums if n > 5]
print("Numbers > 5:", greater_than_5)

# 2. Add 18% tax to sales
sales = [12000, 15500, 9800, 17200, 14300]
with_tax = [s * 1.18 for s in sales]
print("Sales with 18% Tax:", with_tax)

# 3. Filter fruits with more than 5 letters
fruits = ["apple", "banana", "cherry", "kiwi"]
long_fruits = [f for f in fruits if len(f) > 5]
print("Fruits > 5 letters:", long_fruits)

# 4. Uppercase all words
words = ["hello", "world", "python", "data"]
upper_words = [w.upper() for w in words]
print("Uppercase:", upper_words)

# ============================
# Project: Mini Sales Analyzer
# ============================
sales_data = [
    {"product": "Laptop", "price": 50000, "qty": 2, "city": "Delhi"},
    {"product": "Phone", "price": 20000, "qty": 5, "city": "Mumbai"},
    {"product": "Laptop", "price": 50000, "qty": 1, "city": "Mumbai"},
    {"product": "Tablet", "price": 15000, "qty": 3, "city": "Delhi"},
    {"product": "Phone", "price": 20000, "qty": 2, "city": "Delhi"}
]

# Task 1: Total Revenue
total = 0
for row in sales_data:
    revenue = row["price"] * row["qty"]
    total = total + revenue
print("\nTotal Revenue:", total)

# Task 2: High Value Sales (Above 50k)
high_value = [row for row in sales_data if (row["price"] * row["qty"]) > 50000]
print("High Value Sales:", high_value)

# Task 3: City Count
city_counts = {}
for row in sales_data:
    city = row["city"]
    if city in city_counts:
        city_counts[city] = city_counts[city] + 1
    else:
        city_counts[city] = 1
print("City Counts:", city_counts)

# Task 4: Receipts
print("\n--- Receipts ---")
for row in sales_data:
    print(f"{row['product']} sold in {row['city']} for ₹{row['price'] * row['qty']:,}")