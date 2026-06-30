# ---------------- Q94: Compress a string (Run-Length Encoding) ----------------
print("\n--- Q94: Compress string ---")
s = "aaabbbcccd"
result = ""
i = 0
while i < len(s):
    count = 1
    while i + count < len(s) and s[i + count] == s[i]:
        count += 1
    result += s[i] + (str(count) if count > 1 else "")
    i += count
print(f"String: '{s}'")
print(f"Compressed: '{result}'")