# ---------------- Q14: Find nth Fibonacci term ----------------
print("\n--- Q14: Nth Fibonacci term ---")
n = 12
a, b = 0, 1
for _ in range(n - 1):
    a, b = b, a + b
print(f"{n}th Fibonacci term = {a}")
 