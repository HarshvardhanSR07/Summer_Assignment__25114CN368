# ---------------- Q8: Check whether a number is palindrome ----------------
print("\n--- Q8: Palindrome number check ---")
n = 12321
s = str(abs(n))
if s == s[::-1]:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is NOT a Palindrome")
 
 
