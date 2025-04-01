

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# Filter out negative numbers
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("All numbers:", numbers)
print("Positive numbers:", positive_numbers)

# Combine map and filter to get squares of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print("Original numbers:", numbers)
print("Squares of even numbers:", even_squares)