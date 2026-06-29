# Q4. Count digits in a number
def q4_count_digits():
    n = int(input("Enter a number: "))
    count = len(str(abs(n)))
    print(f"Number of digits in {n} = {count}")
 
# q4_count_digits()