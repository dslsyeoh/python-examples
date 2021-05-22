def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"factorial of 5: {factorial(5)}")
print(f"fibonacci of 20: {fibonacci(20)}")

