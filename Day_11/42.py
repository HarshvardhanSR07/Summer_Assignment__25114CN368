# ---------------- Q42: Function to find maximum ----------------
print("\n--- Q42: Maximum of two numbers (function) ---")
def find_max(a, b):
    return a if a >= b else b
a, b = 42, 17
print(f"Maximum of {a} and {b} = {find_max(a, b)}")