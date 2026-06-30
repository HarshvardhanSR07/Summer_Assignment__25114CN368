# ---------------- Q90: Find first repeating character ----------------
print("\n--- Q90: First repeating character ---")
s = "swiss"
seen = set()
result = None
for c in s:
    if c in seen:
        result = c
        break
    seen.add(c)
print(f"String: '{s}'")
print(f"First repeating character = '{result}'" if result else "No repeating character found")
 