# ============================
# Day 8 — File Handling (Read & Write)
# ============================

# 1. Reading a CSV file using the built-in csv module
import csv

print("--- Reading data.csv ---")
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2. Skipping the header (Using slicing [1:])
print("\n--- Reading data.csv (Skipping Header) ---")
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader[1:]: # We'll fix this line if it errors
        print(row)

# 3. Writing to a text file
print("\n--- Writing to results.txt ---")
# 'w' means write mode (it will create the file or overwrite it)
with open("results.txt", "w") as file:
    file.write("Data Analyst Practice\n")
    file.write("Day 8: Writing Files\n")
    file.write("Status: Completed successfully!\n")

print("File written successfully! Check your folder for results.txt")

# 4. Appending to a file
# 'a' means append mode (it adds to the end without deleting old text)
with open("results.txt", "a") as file:
    file.write("This is a new line added later.\n")

print("Appended to file successfully!")