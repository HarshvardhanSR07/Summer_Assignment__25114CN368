# ---------------- Q7: Find product of digits ----------------
print("\n--- Q7: Product of digits ---")
n = 4923
product = 1
for d in str(abs(n)):
    product *= int(d)
print(f"Product of digits of {n} = {product}")
 
