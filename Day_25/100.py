# ---------------- Q100: Sort words by length ----------------
print("\n--- Q100: Sort words by length ---")
s = "Python is a powerful programming language"
words = s.split()
print(f"Original words: {words}")
words.sort(key=len)
print(f"Sorted by length: {words}")
 