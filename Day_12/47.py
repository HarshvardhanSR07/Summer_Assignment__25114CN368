# ---------------- Q47: Function for Fibonacci ----------------
print("\n--- Q47: Fibonacci series (function) ---")
def fibonacci_fn(num):
    a, b = 0, 1
    series = []
    for _ in range(num):
        series.append(a)
        a, b = b, a + b
    return series
n = 10
print(f"Fibonacci series: {fibonacci_fn(n)}")
 