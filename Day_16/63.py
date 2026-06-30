# ---------------- Q63: Find pair with given sum ----------------
print("\n--- Q63: Pair with given sum ---")
arr = [2, 7, 11, 15, 4, 9]
target = 13
seen = set()
pairs = []
for x in arr:
    complement = target - x
    if complement in seen:
        pairs.append((complement, x))
    seen.add(x)
print(f"Array: {arr}, Target sum: {target}")
print(f"Pairs found: {pairs}")
 