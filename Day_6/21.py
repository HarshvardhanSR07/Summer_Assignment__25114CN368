# ---------------- Q21: Convert decimal to binary ----------------
print("\n--- Q21: Decimal to binary ---")
n = 156
temp = abs(n)
binary = ""
if temp == 0:
    binary = "0"
while temp > 0:
    binary = str(temp % 2) + binary
    temp //= 2
print(f"Binary of {n} = {binary}")
 