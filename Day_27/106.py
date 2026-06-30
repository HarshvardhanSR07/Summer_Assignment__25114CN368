# ---------------- Q106: Employee management system ----------------
print("\n--- Q106: Employee management ---")
employees = []
employees.append({"id": "E1", "name": "Vikram", "dept": "IT", "salary": 55000})
employees.append({"id": "E2", "name": "Sneha", "dept": "HR", "salary": 48000})
print("All Employees:")
for e in employees:
    print(f"  ID: {e['id']}, Name: {e['name']}, Dept: {e['dept']}, Salary: Rs {e['salary']}")