#--------------- Q5: Sum of digits of a number ----------------
print("\n--- Q5: Sum of digits ---")
n = 48293
total = sum(int(d) for d in str(abs(n)))
print(f"Sum of digits of {n} = {total}")
 
