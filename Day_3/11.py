# ---------------- Q11: Find GCD of two numbers ----------------
print("\n--- Q11: GCD of two numbers ---")
a, b = 54, 24
x, y = a, b
while y:
    x, y = y, x % y
print(f"GCD of {a} and {b} = {x}")
 