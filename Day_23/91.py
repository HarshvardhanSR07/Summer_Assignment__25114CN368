# ---------------- Q91: Check anagram strings ----------------
print("\n--- Q91: Anagram check ---")
s1 = "listen"
s2 = "silent"
print(f"String 1: '{s1}', String 2: '{s2}'")
print("Anagrams" if sorted(s1) == sorted(s2) else "NOT Anagrams")