# ---------------- Q64: Remove duplicates from array ----------------
print("\n--- Q64: Remove duplicates ---")
arr = [4, 2, 7, 4, 9, 4, 2, 1]
unique = []
for x in arr:
    if x not in unique:
        unique.append(x)
print(f"Original: {arr}")
print(f"Without duplicates: {unique}")
 