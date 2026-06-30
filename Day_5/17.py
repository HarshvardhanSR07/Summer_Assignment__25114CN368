# ---------------- Q17: Check perfect number ----------------
print("\n--- Q17: Perfect number check ---")
n = 28
divisors_sum = sum(i for i in range(1, n) if n % i == 0)
print(f"{n} is {'a Perfect' if divisors_sum == n else 'NOT a Perfect'} number")
 