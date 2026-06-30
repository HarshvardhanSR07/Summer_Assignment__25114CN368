# ---------------- Q102: Voting eligibility system ----------------
print("\n--- Q102: Voting eligibility ---")
name, age = "Rahul", 20
if age >= 18:
    print(f"{name}, you ARE eligible to vote.")
else:
    print(f"{name}, you are NOT eligible. Need {18 - age} more year(s).")