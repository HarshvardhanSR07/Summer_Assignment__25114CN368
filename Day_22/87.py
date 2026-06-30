# ---------------- Q87: Character frequency ----------------
print("\n--- Q87: Character frequency ---")
s = "programming"
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print(f"String: '{s}'")
print("Character frequencies:")
for char, cnt in sorted(freq.items()):
    print(f"  '{char}' : {cnt}")
 