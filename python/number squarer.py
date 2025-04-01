def square_numbers(numbers):
    return [num ** 2 for num in numbers]

# Example usage
numbers = [1, 2, 3, 4, 5]
squared = square_numbers(numbers)
print("Original numbers:", numbers)
print("Squared numbers:", squared)

# Using lambda and map
squared_lambda = list(map(lambda x: x**2, numbers))
print("Squared using lambda and map:", squared_lambda)

# Using lambda and filter (to get only even squares)
even_squares = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print("Even squares using lambda, map, and filter:", even_squares)