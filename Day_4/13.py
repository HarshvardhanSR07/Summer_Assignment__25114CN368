# ---------------- Q13: Generate Fibonacci series ----------------
print("\n--- Q13: Fibonacci series ---")
n = 10
a, b = 0, 1
series = []
for _ in range(n):
    series.append(a)
    a, b = b, a + b
print(f"First {n} Fibonacci terms: {series}")
 