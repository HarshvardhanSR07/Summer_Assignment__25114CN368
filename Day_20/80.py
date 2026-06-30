# ---------------- Q80: Column-wise Sum ----------------
print("\n--- Q80: Column-wise Sum ---")

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(A)
cols = len(A[0])

print("Matrix:", A)

for j in range(cols):
    col_sum = 0

    for i in range(rows):
        col_sum = col_sum + A[i][j]

    print("Sum of column", j + 1, "=", col_sum)