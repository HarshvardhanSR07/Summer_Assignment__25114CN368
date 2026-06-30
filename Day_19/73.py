# ---------------- Q73: Add matrices ----------------
print("\n--- Q73: Add matrices ---")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
rows, cols = len(A), len(A[0])
result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
print(f"A = {A}\nB = {B}")
print(f"A + B = {result}")