# ---------------- Q40: Print character pyramid ----------------
print("\n--- Q40: Character pyramid ---")
rows = 5
for i in range(1, rows + 1):
    left = "".join(chr(64 + x) for x in range(1, i + 1))
    right = "".join(chr(64 + x) for x in range(i - 1, 0, -1))
    print(" " * (rows - i) + left + right)
 
 