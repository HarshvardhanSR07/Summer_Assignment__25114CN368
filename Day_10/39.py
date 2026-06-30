# ---------------- Q39: Print number pyramid ----------------
print("\n--- Q39: Number pyramid ---")
rows = 5
for i in range(1, rows + 1):
    left = "".join(str(x) for x in range(1, i + 1))
    right = "".join(str(x) for x in range(i - 1, 0, -1))
    print(" " * (rows - i) + left + right)
 