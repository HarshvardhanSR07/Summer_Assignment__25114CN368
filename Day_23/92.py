# ---------------- Q92: Find maximum occurring character ----------------
print("\n--- Q92: Maximum occurring character ---")
s = "programming"
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
max_char = max(freq, key=freq.get)
print(f"String: '{s}'")
print(f"Maximum occurring character = '{max_char}' ({freq[max_char]} times)")
 