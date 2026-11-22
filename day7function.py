# ============================
# Day 7 — Functions
# ============================

# 1. Function for calculation (Returning a value)
def calculate_revenue(price, qty):
    total = price * qty
    return total

# Call the function
revenue = calculate_revenue(500, 3)
print("Revenue 1:", revenue)

# You can reuse it!
revenue2 = calculate_revenue(200, 10)
print("Revenue 2:", revenue2)


# 2. Function for cleaning text (Returning a string)
def clean_name(name):
    return name.strip().title()

# Call the function
clean = clean_name("  rohan kumar  ")
print("\nCleaned Name:", clean)


# 3. Function with a Condition (Returning True/False)
def is_high_value(price):
    if price > 50000:
        return True
    else:
        return False

# Call the function
check1 = is_high_value(60000)
check2 = is_high_value(20000)

print("\nIs 60,000 high value?", check1)
print("Is 20,000 high value?", check2)


# 4. Real-world usage of functions
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

final = calculate_discount(1000, 20)
print(f"\nFinal price after 20% discount: ₹{final}")