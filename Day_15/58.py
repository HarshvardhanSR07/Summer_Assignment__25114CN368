# ---------------- Q58: Rotate array left ----------------
print("\n--- Q58: Rotate array left ---")
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
n = len(arr)
k = k % n
rotated = arr[k:] + arr[:k]
print(f"Original: {arr}, Rotate left by {k}: {rotated}")
 