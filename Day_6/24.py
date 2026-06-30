# ---------------- Q24: Find x^n without pow() ----------------
print("\n--- Q24: x^n without pow() ---")
x, n = 3, 7
result = 1
base, exp = x, abs(n)
while exp > 0:
    if exp % 2 == 1:
        result *= base
    base *= base
    exp //= 2
if n < 0:
    result = 1 / result
print(f"{x}^{n} = {result}")
 
 