# ---------------- Q78: Check symmetric matrix ----------------
print("\n--- Q78: Symmetric matrix check ---")
A = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
n = len(A)
T = [[A[j][i] for j in range(n)] for i in range(n)]
print(f"Matrix: {A}")
print("Symmetric" if A == T else "NOT Symmetric")
 