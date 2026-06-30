# ---------------- Q12: Find LCM of two numbers ----------------
print("\n--- Q12: LCM of two numbers ---")
a, b = 12, 18
x, y = a, b
while y:
    x, y = y, x % y
gcd = x
lcm = (a * b) // gcd
print(f"LCM of {a} and {b} = {lcm}")
 
 