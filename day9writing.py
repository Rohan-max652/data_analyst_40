# ============================
# Day 9 — Writing to Files
# ============================

# 1. Writing multiple lines to a text file
import csv
print("--- Writing to results.txt ---")

with open("results.txt", "w") as file:
    file.write("Data Analyst Practice\n")
    file.write("Day 9: Writing Files\n")
    file.write("Status: Completed successfully!\n")

print("File 'results.txt' created and saved!")

# 2. Appending to the file (Adding without deleting)
# 'a' means append mode
print("\n--- Appending to results.txt ---")

with open("results.txt", "a") as file:
    file.write("Day 10 is next.\n")
    file.write("I am becoming a Data Analyst.\n")

print("New lines appended to 'results.txt'!")


# 3. Real-world example: Writing data to a CSV file
print("\n--- Writing to a CSV file ---")

# A list of lists representing rows
data = [
    ["Name", "Age", "City"],
    ["Rohan", "24", "Delhi"],
    ["Priya", "22", "Mumbai"],
    ["Amit", "27", "Bangalore"]
]

# Write to a CSV file
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)  # We need to import csv for this!
    writer.writerows(data)

print("File 'output.csv' created and saved!")