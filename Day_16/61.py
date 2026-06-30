# ---------------- Q61: Find missing number in array ----------------
print("\n--- Q61: Missing number (1 to N) ---")
n = 8
arr = [1, 2, 4, 5, 6, 7, 8]   # 3 is missing
expected = n * (n + 1) // 2
missing = expected - sum(arr)
print(f"Array: {arr} (expected 1 to {n})")
print(f"Missing number = {missing}")
 