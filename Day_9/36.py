# ---------------- Q36: Print hollow square pattern ----------------
print("\n--- Q36: Hollow square pattern ---")
n = 5
for i in range(n):
    line = ""
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            line += "*"
        else:
            line += " "
    print(line)
 
 