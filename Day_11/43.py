# ---------------- Q43: Function to check prime ----------------
print("\n--- Q43: Prime check (function) ---")
def is_prime_fn(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
n = 37
print(f"{n} is {'a Prime' if is_prime_fn(n) else 'NOT a Prime'} number")
 