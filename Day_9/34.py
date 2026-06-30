#---------- Q34: Print reverse number triangle ----------------
print("\n--- Q34: Reverse number triangle ---")
rows = 5
for i in range(rows, 0, -1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    print(line)
 