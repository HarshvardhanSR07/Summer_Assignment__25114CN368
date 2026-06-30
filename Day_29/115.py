# ---------------- Q115: Menu-Driven String Operations System ----------------
print("\n--- Q115: Menu-Driven String Operations System ---")

s = "Hello Python"

print("Original String:", s)

# Find length
length = len(s)
print("Length:", length)

# Reverse the string
reverse = ""
for i in range(length - 1, -1, -1):
    reverse = reverse + s[i]

print("Reversed String:", reverse)

# Convert to uppercase
upper = s.upper()
print("Uppercase:", upper)

# Convert to lowercase
lower = s.lower()
print("Lowercase:", lower)

# Count words
word_count = 1

for ch in s:
    if ch == " ":
        word_count = word_count + 1

print("Word Count:", word_count)