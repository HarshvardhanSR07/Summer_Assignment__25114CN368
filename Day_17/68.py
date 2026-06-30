# ---------------- Q68: Find Common Elements ----------------
print("\n--- Q68: Common Elements (3 Arrays) ---")

arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 4, 5]
arr3 = [3, 4, 5, 6]

common = []

# Check elements from first array
for x in arr1:
    if x in arr2 and x in arr3:
        if x not in common:
            common.append(x)

# Optional: sort manually (bubble sort)
for i in range(len(common)):
    for j in range(len(common) - 1):
        if common[j] > common[j + 1]:
            temp = common[j]
            common[j] = common[j + 1]
            common[j + 1] = temp

print("Array1:", arr1)
print("Array2:", arr2)
print("Array3:", arr3)
print("Common elements:", common)