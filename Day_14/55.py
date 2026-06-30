# ---------------- Q55: Second largest element ----------------
print("\n--- Q55: Second largest element ---")
arr = [12, 45, 7, 23, 56, 89, 34]
unique = sorted(set(arr), reverse=True)
print(f"Array: {arr}")
print(f"Second largest = {unique[1]}")
 