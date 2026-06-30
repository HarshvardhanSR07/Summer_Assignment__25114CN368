# ---------------- Q98: Find common characters in strings ----------------
print("\n--- Q98: Common characters ---")
s1 = "programming"
s2 = "marketing"
common = sorted(set(s1) & set(s2))
print(f"String1: '{s1}', String2: '{s2}'")
print(f"Common characters: {common}")