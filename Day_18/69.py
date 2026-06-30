# ---------------- Q69: Bubble sort ----------------
print("\n--- Q69: Bubble sort ---")
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(f"Sorted (Bubble Sort): {arr}")