# ---------------- Q27: Recursive sum of digits ----------------
print("\n--- Q27: Recursive sum of digits ---")
def sum_digits_recursive(k):
    k = abs(k)
    if k < 10:
        return k
    return k % 10 + sum_digits_recursive(k // 10)
n = 48293
print(f"Sum of digits of {n} = {sum_digits_recursive(n)}")
 