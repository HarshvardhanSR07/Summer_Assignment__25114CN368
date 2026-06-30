# ---------------- Q30: Print number triangle ----------------
print("\n--- Q30: Number triangle ---")
rows = 5
for i in range(1, rows + 1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    print(line)
 