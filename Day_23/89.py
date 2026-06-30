# ---------------- Q89: Find first non-repeating character ----------------
print("\n--- Q89: First Non-Repeating Character ---")

s = "swiss"
freq = {}

# Count the frequency of each character
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find the first character with frequency 1
result = None

for ch in s:
    if freq[ch] == 1:
        result = ch
        break

print("String:", s)

if result is not None:
    print("First non-repeating character =", result)
else:
    print("No non-repeating character found")