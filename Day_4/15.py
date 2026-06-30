# ---------------- Q15: Check Armstrong number ----------------
print("\n--- Q15: Armstrong number check ---")
n = 153
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)
print(f"{n} is {'an Armstrong' if total == n else 'NOT an Armstrong'} number")
 