# ---------------- Q9: Check whether a number is prime ----------------
print("\n--- Q9: Prime number check ---")
n = 29
is_prime = n >= 2
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(f"{n} is {'a Prime' if is_prime else 'NOT a Prime'} number")