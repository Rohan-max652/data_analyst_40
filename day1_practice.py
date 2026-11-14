
# DAY 1 — Python Foundations


# --- Basics ---
a = 10
print(a)

# --- Data Types ---
name = "Rahul"
age = 24
salary = 45000.50
is_analyst = True
print(type(name), type(age), type(salary), type(is_analyst))

# --- Type Casting ---
raw_price = "1299.50"
price = float(raw_price)
print(price)

# --- Operators ---
print(10 + 3)
print(10 % 3)

# --- Conditions ---
sales = 85000
if sales >= 100000:
    print("Excellent")
elif sales >= 50000:
    print("Good")
else:
    print("Needs improvement")

# --- Loops ---
for i in range(5):
    print("Order", i + 1)

# --- Input / Output ---
# name = input("Enter name: ")
# print(f"Hello {name}")

# --- Practice: Arithmetic ---
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")