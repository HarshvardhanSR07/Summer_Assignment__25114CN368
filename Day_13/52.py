# ---------------- Q52: Count Even and Odd Elements ----------------
print("\n--- Q52: Count Even and Odd Elements ---")

arr = [12, 45, 7, 23, 56, 89, 34]

even_count = 0
odd_count = 0

for x in arr:
    if x % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Array:", arr)
print("Even elements:", even_count)
print("Odd elements:", odd_count)