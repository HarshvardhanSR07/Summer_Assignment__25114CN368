# ---------------- Q53: Linear search ----------------
print("\n--- Q53: Linear search ---")
arr = [12, 45, 7, 23, 56, 89, 34]
key = 56
found = False
for i, val in enumerate(arr):
    if val == key:
        print(f"{key} found at index {i}")
        found = True
        break
if not found:
    print(f"{key} not found in array")
 