# ---------------- Q18: Check strong number ----------------
print("\n--- Q18: Strong number check ---")
n = 145
total = 0
for d in str(n):
    fact = 1
    for i in range(1, int(d) + 1):
        fact *= i
    total += fact
print(f"{n} is {'a Strong' if total == n else 'NOT a Strong'} number")
 