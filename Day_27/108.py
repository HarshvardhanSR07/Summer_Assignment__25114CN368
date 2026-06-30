# ---------------- Q108: Marksheet Generation System ----------------
print("\n--- Q108: Marksheet Generation System ---")

name = "Aisha Khan"
roll = "CS101"

subjects = ["Maths", "Physics", "Chemistry", "English", "CS"]
marks = [85, 78, 92, 80, 95]

# Calculate total marks
total = 0
for mark in marks:
    total += mark

# Calculate percentage
percentage = total / len(marks)

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
else:
    grade = "C"

# Display marksheet
print("Name:", name)
print("Roll No.:", roll)

print("\nMarks:")
for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("\nTotal Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)