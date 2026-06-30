# ---------------- Q22: Convert binary to decimal ----------------
print("\n--- Q22: Binary to decimal ---")
binary = "10011100"
decimal = 0
for bit in binary:
    decimal = decimal * 2 + int(bit)
print(f"Decimal of {binary} = {decimal}")
 