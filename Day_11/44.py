# ---------------- Q44: Function to find factorial ----------------
print("\n--- Q44: Factorial (function) ---")
def factorial_fn(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result
n = 7
print(f"Factorial of {n} = {factorial_fn(n)}")
 
 