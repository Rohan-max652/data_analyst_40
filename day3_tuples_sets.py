import pandas as pd

# Table 1: Employees
employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Rohan", "Priya", "Amit"],
    "DeptID": [10, 20, 10]
})

# Table 2: Departments
departments = pd.DataFrame({
    "DeptID": [10, 20, 30],
    "DeptName": ["IT", "HR", "Sales"]
})

# Merge them!
print("--- Merged Table ---")
merged_data = pd.merge(employees, departments, on="DeptID")
print(merged_data)