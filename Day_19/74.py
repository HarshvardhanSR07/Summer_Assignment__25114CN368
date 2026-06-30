# ---------------- Q74: Subtract matrices ----------------
print("\n--- Q74: Subtract matrices ---")

A = [[5, 6], [7, 8]]
B = [[1, 2], [3, 4]]

rows = len(A)
cols = len(A[0])

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] - B[i][j])
    result.append(row)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nA - B:")
for row in result:
    print(row)