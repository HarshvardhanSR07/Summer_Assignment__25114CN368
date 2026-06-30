# ---------------- Q83: Count Vowels and Consonants ----------------
print("\n--- Q83: Vowels and Consonants ---")

s = "Hello World"
sl = s.lower()

vowels_list = "aeiou"

vowels = 0
consonants = 0

for c in sl:
    if c.isalpha():
        if c in vowels_list:
            vowels += 1
        else:
            consonants += 1

print("String:", s)
print("Vowels =", vowels)
print("Consonants =", consonants)