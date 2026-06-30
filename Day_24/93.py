# ---------------- Q93: Check string rotation ----------------
print("\n--- Q93: String rotation check ---")
s1 = "waterbottle"
s2 = "erbottlewat"
result = len(s1) == len(s2) and s2 in (s1 + s1)
print(f"String 1: '{s1}', String 2: '{s2}'")
print(f"'{s2}' is {'a rotation' if result else 'NOT a rotation'} of '{s1}'")
 