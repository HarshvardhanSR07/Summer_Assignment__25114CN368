# ---------------- Q6: Reverse a number ----------------
print("\n--- Q6: Reverse a number ---")
n = 123456
sign = -1 if n < 0 else 1
reversed_n = sign * int(str(abs(n))[::-1])
print(f"Reversed number of {n} = {reversed_n}")
 
