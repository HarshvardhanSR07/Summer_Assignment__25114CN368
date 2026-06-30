# ---------------- Q76: Find Diagonal Sum ----------------
print("\n--- Q76: Diagonal Sum ---")

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(A)

main_diag = 0
anti_diag = 0

for i in range(n):
    main_diag = main_diag + A[i][i]
    anti_diag = anti_diag + A[i][n - 1 - i]

print("Matrix:", A)
print("Main diagonal sum =", main_diag)
print("Anti diagonal sum =", anti_diag)