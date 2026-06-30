# ---------------- Q20: Find largest prime factor ----------------
print("\n--- Q20: Largest prime factor ---")
n = 13195
largest = -1
d = 2
temp = n
while d * d <= temp:
    while temp % d == 0:
        largest = d
        temp //= d
    d += 1
if temp > 1:
    largest = temp
print(f"Largest prime factor of {n} = {largest}")
 
 