# ---------------- Q16: Print Armstrong numbers in a range ----------------
print("\n--- Q16: Armstrong numbers in a range ---")
start, end = 1, 1000
armstrongs = []
for num in range(start, end + 1):
    digits = str(num)
    power = len(digits)
    if sum(int(d) ** power for d in digits) == num:
        armstrongs.append(num)
print(f"Armstrong numbers between {start} and {end}: {armstrongs}")
 
 