# ---------------- Q31: Print character triangle ----------------
print("\n--- Q31: Character triangle ---")
rows = 5
for i in range(1, rows + 1):
    line = ""
    for j in range(i):
        line += chr(65 + j)
    print(line)
 