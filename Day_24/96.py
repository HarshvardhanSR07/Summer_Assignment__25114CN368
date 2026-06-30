# ---------------- Q96: Remove duplicate characters ----------------
print("\n--- Q96: Remove duplicate characters ---")
s = "programming"
seen = set()
result = ""
for c in s:
    if c not in seen:
        result += c
        seen.add(c)
print(f"String: '{s}'")
print(f"Without duplicates: '{result}'")
 