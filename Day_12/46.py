# ---------------- Q46: Function for Armstrong ----------------
print("\n--- Q46: Armstrong (function) ---")
def is_armstrong_fn(num):
    digits = str(num)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == num
n = 371
print(f"{n} is {'an Armstrong' if is_armstrong_fn(n) else 'NOT an Armstrong'} number")
 