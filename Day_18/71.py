
# ---------------- Q71: Binary search ----------------
print("\n--- Q71: Binary search ---")
arr = [11, 12, 22, 25, 34, 64, 90]
key = 25
lo, hi = 0, len(arr) - 1
found = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == key:
        found = mid
        break
    elif arr[mid] < key:
        lo = mid + 1
    else:
        hi = mid - 1
print(f"Sorted array: {arr}, Searching for: {key}")
print(f"Found at index {found}" if found != -1 else "Not found")