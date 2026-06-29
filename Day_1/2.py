 #Q2. Multiplication table of a given number
def q2_multiplication_table():
    n = int(input("Enter a number: "))
    print(f"\nMultiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
# This is the second program
 