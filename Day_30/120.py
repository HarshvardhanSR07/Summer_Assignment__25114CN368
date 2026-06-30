# ---------------- Q120: Complete Mini Project — Student Grade Tracker ----------------
print("\n--- Q120: Student Grade Tracker ---")

subjects = ["Maths", "Science", "English", "Hindi", "CS"]

rolls = ["1", "2"]
names = ["Aisha", "Rahul"]
classes = ["10-A", "10-A"]

marks = [
    [88, 92, 79, 85, 95],
    [60, 55, 40, 65, 30]
]

topper_index = 0
topper_total = 0

print("\n--- REPORT CARDS ---")

for i in range(len(names)):

    # Total
    total = 0
    for j in range(len(marks[i])):
        total = total + marks[i][j]

    # Percentage
    percent = total / len(marks[i])

    # Grade
    if percent >= 90:
        grade = "A+"
    elif percent >= 75:
        grade = "A"
    elif percent >= 60:
        grade = "B"
    elif percent >= 45:
        grade = "C"
    elif percent >= 33:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail
    result = "PASS"
    for m in marks[i]:
        if m < 33:
            result = "FAIL"
            break

    print("\nREPORT CARD:", names[i], "(Roll", rolls[i], ", Class", classes[i], ")")

    for j in range(len(subjects)):
        print(subjects[j], ":", marks[i][j])

    print("Total:", total)
    print("Percentage:", round(percent, 2), "%")
    print("Grade:", grade)
    print("Result:", result)

    # Topper tracking
    if total > topper_total:
        topper_total = total
        topper_index = i


print("\nClass Topper:", names[topper_index], "(Total:", topper_total, ")")

# Subject-wise analysis
print("\nSubject-wise Class Analysis:")

for i in range(len(subjects)):

    total_sub = 0
    highest = marks[0][i]
    lowest = marks[0][i]

    for j in range(len(names)):
        score = marks[j][i]
        total_sub = total_sub + score

        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

    avg = total_sub / len(names)

    print(subjects[i], ": Avg =", round(avg, 2),
          ", Highest =", highest,
          ", Lowest =", lowest)