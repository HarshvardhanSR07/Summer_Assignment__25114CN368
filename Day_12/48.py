# ---------------- Q48: Perfect Number (Function) ----------------
print("\n--- Q48: Perfect Number (Function) ---")

def is_perfect_fn(num):
    if num <= 0:
        return False

    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        return True
    else:
        return False

n = 496

if is_perfect_fn(n):
    print(n, "is a Perfect number")
else:
    print(n, "is NOT a Perfect number")