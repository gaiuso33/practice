import math
def circle_area(radius):
    return math.pi * radius**2
def rectangle_area(length, width):
    return length * width
def triangle_area(base, height):
    return 0.5 * base * height
def square_area(side):
    return side**2
while True:
    print("\nShape Area Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Quit")
    choice = input("Enter your choice (1/2/3/4/5): ")    
    if choice == '5':
        print("Thank you for using the shape area calculator. Goodbye!")
        break
    
    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print(f"The area of the circle is {area:.2f}")
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print(f"The area of the rectangle is {area:.2f}")
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
        print(f"The area of the triangle is {area:.2f}")
    elif choice == '4':
        side = float(input("Enter the side length of the square: "))
        area = square_area(side)
        print(f"The area of the square is {area:.2f}")
    else:
        print("Invalid choice. Please try again.")