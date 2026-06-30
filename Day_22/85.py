# ---------------- Q85: Check palindrome string ----------------
print("\n--- Q85: Palindrome string check ---")
s = "madam"
sl = s.lower().replace(" ", "")
print(f"String: '{s}'")
print("Palindrome" if sl == sl[::-1] else "NOT Palindrome")
 