# ---------------- Q56: Find Duplicates in Array ----------------
print("\n--- Q56: Find Duplicates ---")

arr = [4, 2, 7, 4, 9, 4, 2, 1]

duplicates = []

# Check each element
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            if arr[i] not in duplicates:
                duplicates.append(arr[i])

print("Array:", arr)
print("Duplicates:", duplicates)