# ---------------- Q19: Print factors of a number ----------------
print("\n--- Q19: Factors of a number ---")
n = 36
factors = [i for i in range(1, n + 1) if n % i == 0]
print(f"Factors of {n}: {factors}")
 