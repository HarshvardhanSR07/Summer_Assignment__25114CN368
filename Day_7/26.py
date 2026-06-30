# ---------------- Q26: Recursive Fibonacci ----------------
print("\n--- Q26: Recursive Fibonacci ---")
def fib_recursive(k):
    if k <= 0:
        return 0
    if k == 1:
        return 1
    return fib_recursive(k - 1) + fib_recursive(k - 2)
n = 10
print(f"Fibonacci({n}) = {fib_recursive(n)}")
 