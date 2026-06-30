# ---------------- Q105: Student record management system ----------------
print("\n--- Q105: Student record management ---")
students = []
students.append({"roll": "101", "name": "Aisha", "marks": 88})
students.append({"roll": "102", "name": "Rahul", "marks": 76})
print("All Students:")
for s in students:
    print(f"  Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
search_roll = "101"
found = [s for s in students if s["roll"] == search_roll]
print(f"Search Roll {search_roll}: {found[0] if found else 'Not found'}")