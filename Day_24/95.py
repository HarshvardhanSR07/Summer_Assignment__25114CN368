# ---------------- Q95: Find longest word ----------------
print("\n--- Q95: Longest word ---")
s = "Python is a powerful programming language"
words = s.split()
longest = max(words, key=len)
print(f"Sentence: '{s}'")
print(f"Longest word = '{longest}' (length {len(longest)})")