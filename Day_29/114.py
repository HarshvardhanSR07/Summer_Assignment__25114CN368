# ---------------- Q114: Menu-Driven Array Operations System ----------------
print("\n--- Q114: Menu-Driven Array Operations System ---")

arr = [34, 12, 67, 23, 9]

print("Original Array:", arr)

# Sum and Average
total = 0
for num in arr:
    total = total + num

average = total / len(arr)

# Minimum and Maximum
minimum = arr[0]
maximum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

# Reverse Array
print("Reversed Array:")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()

# Ascending Order (Bubble Sort)
ascending = arr.copy()

for i in range(len(ascending)):
    for j in range(len(ascending) - 1 - i):
        if ascending[j] > ascending[j + 1]:
            temp = ascending[j]
            ascending[j] = ascending[j + 1]
            ascending[j + 1] = temp

print("Sorted Ascending:", ascending)

# Descending Order
descending = ascending.copy()

for i in range(len(descending) // 2):
    temp = descending[i]
    descending[i] = descending[len(descending) - 1 - i]
    descending[len(descending) - 1 - i] = temp

print("Sorted Descending:", descending)

print("Sum =", total)
print("Average =", average)
print("Minimum =", minimum)
print("Maximum =", maximum)