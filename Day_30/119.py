# ---------------- Q119: Mini Employee Management System ----------------
print("\n--- Q119: Mini Employee Management System ---")

emp_ids = ["E1", "E2", "E3"]
names = ["Vikram", "Sneha", "Karan"]
depts = ["IT", "HR", "Finance"]
salaries = [55000, 48000, 62000]

# Sort employees by salary (manual selection sort - descending)
n = len(salaries)

for i in range(n):
    for j in range(i + 1, n):
        if salaries[i] < salaries[j]:
            # swap salaries
            temp = salaries[i]
            salaries[i] = salaries[j]
            salaries[j] = temp

            # swap names
            temp = names[i]
            names[i] = names[j]
            names[j] = temp

            # swap departments
            temp = depts[i]
            depts[i] = depts[j]
            depts[j] = temp

            # swap IDs
            temp = emp_ids[i]
            emp_ids[i] = emp_ids[j]
            emp_ids[j] = temp

print("Employees sorted by salary (highest first):")

for i in range(n):
    print(names[i], "(", depts[i], "): Rs", salaries[i])

# Calculate average salary
total_salary = 0
for sal in salaries:
    total_salary = total_salary + sal

average_salary = total_salary / n

print("\nAverage Salary: Rs", round(average_salary, 2))