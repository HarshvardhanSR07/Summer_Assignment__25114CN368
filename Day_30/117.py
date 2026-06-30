
# ---------------- Q117: Student record system using arrays and strings ----------------
print("\n--- Q117: Student record system (arrays + strings) ---")
subjects = ["Maths", "Physics", "Chemistry", "English", "CS"]
students = [
    {"roll": "101", "name": "Aisha", "marks": [85, 78, 92, 80, 95]},
    {"roll": "102", "name": "Rahul", "marks": [60, 55, 40, 65, 70]},
]
for s in students:
    total = sum(s["marks"])
    percent = total / len(s["marks"])
    result = "PASS" if all(m >= 33 for m in s["marks"]) else "FAIL"
    print(f"  {s['name']} (Roll {s['roll']}): Total={total}, %={percent:.2f}, {result}")
topper = max(students, key=lambda s: sum(s["marks"]))
print(f"Topper: {topper['name']}")
 