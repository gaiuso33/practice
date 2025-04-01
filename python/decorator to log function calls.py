import functools
import time

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} returned: {result}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        print("-" * 40)
        return result
    return wrapper

@log_function_call
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@log_function_call
def add(a, b):
    return a + b

# Test the decorated functions
print("Testing factorial function:")
factorial(5)

print("\nTesting add function:")
add(3, 4)