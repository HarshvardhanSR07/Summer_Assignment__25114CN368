# ---------------- Q75: Transpose matrix ----------------
print("\n--- Q75: Transpose matrix ---")
A = [[1, 2, 3], [4, 5, 6]]
rows, cols = len(A), len(A[0])
T = [[A[i][j] for i in range(rows)] for j in range(cols)]
print(f"A = {A}")
print(f"Transpose = {T}")
 