
employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

adjust_salary = lambda employee: employee.update({"salary": employee["salary"] * 1.10}) if employee["rating"] >= 4 else employee.update({"salary": employee["salary"] * 1.05}) if employee["rating"] == 3 else employee.update({"salary": employee["salary"] * 0.97}) or employee
list(map(adjust_salary, employees))
print(employees)
