# ---------------- Q25: Recursive factorial ----------------
print("\n--- Q25: Recursive factorial ---")
def fact_recursive(k):
    if k == 0 or k == 1:
        return 1
    return k * fact_recursive(k - 1)
n = 6
print(f"Factorial of {n} = {fact_recursive(n)}")
 