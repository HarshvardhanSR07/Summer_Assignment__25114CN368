# ---------------- Q59: Rotate array right ----------------
print("\n--- Q59: Rotate array right ---")
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
n = len(arr)
k = k % n
rotated = arr[n - k:] + arr[:n - k]
print(f"Original: {arr}, Rotate right by {k}: {rotated}")
 