# Q3. Factorial of a number
def q3_factorial():
    n = int(input("Enter a number: "))
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"Factorial of {n} = {result}")
 
# q3_factorial()
 