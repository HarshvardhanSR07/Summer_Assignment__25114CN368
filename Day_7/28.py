# ---------------- Q28: Recursive reverse number ----------------
print("\n--- Q28: Recursive reverse number ---")
def reverse_recursive(k, rev=0):
    if k == 0:
        return rev
    return reverse_recursive(k // 10, rev * 10 + k % 10)
n = 123456
result = reverse_recursive(abs(n))
if n < 0:
    result = -result
print(f"Reversed number of {n} = {result}")
 
 