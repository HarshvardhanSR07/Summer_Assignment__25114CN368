# ---------------- Q60: Move Zeroes to End ----------------
print("\n--- Q60: Move Zeroes to End ---")

arr = [0, 1, 0, 3, 12, 0, 5]

non_zero = []
zero_count = 0

# Separate non-zero elements and count zeros
for x in arr:
    if x != 0:
        non_zero.append(x)
    else:
        zero_count = zero_count + 1

# Create zero list
zeros = []
for i in range(zero_count):
    zeros.append(0)

# Combine both
result = non_zero + zeros

print("Original:", arr)
print("After moving zeroes:", result)