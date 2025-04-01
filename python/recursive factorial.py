def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Test the factorial function
numbers = [0, 1, 5, 10]
for num in numbers:
    result = factorial(num)
    print(f"Factorial of {num} is {result}")