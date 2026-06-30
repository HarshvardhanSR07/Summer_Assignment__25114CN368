# ---------------- Q10: Print prime numbers in a range ----------------
print("\n--- Q10: Primes in a range ---")
start, end = 10, 50
primes = []
for num in range(max(2, start), end + 1):
    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        primes.append(num)
print(f"Prime numbers between {start} and {end}: {primes}")
 