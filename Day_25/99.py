# ---------------- Q99: Sort names alphabetically ----------------
print("\n--- Q99: Sort names alphabetically ---")
names = ["Rahul", "amit", "Priya", "kunal", "Aisha"]
print(f"Original: {names}")
names.sort(key=str.lower)
print(f"Sorted: {names}")