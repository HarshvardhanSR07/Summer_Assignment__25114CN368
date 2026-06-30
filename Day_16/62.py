# ---------------- Q62: Find maximum frequency element ----------------
print("\n--- Q62: Maximum frequency element ---")
arr = [4, 2, 7, 4, 9, 4, 2, 1]
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
max_elem = max(freq, key=freq.get)
print(f"Array: {arr}")
print(f"Maximum frequency element = {max_elem} (appears {freq[max_elem]} times)")
 