# ---------------- Q79: Find row-wise sum ----------------
print("\n--- Q79: Row-wise sum ---")
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {A}")
for i, row in enumerate(A):
    print(f"Sum of row {i + 1} = {sum(row)}")
 