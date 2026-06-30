# ---------------- Q45: Function for palindrome ----------------
print("\n--- Q45: Palindrome (function) ---")
def is_palindrome_fn(num):
    s = str(abs(num))
    return s == s[::-1]
n = 12321
print(f"{n} is {'a Palindrome' if is_palindrome_fn(n) else 'NOT a Palindrome'}")
 