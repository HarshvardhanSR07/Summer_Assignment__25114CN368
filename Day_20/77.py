# ---------------- Q77: Multiply matrices ----------------
print("\n--- Q77: Multiply matrices ---")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
r1, c1, c2 = len(A), len(A[0]), len(B[0])
result = [[sum(A[i][k] * B[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]
print(f"A = {A}\nB = {B}")
print(f"A x B = {result}")
 