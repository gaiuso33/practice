def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
while True:
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '3':
        print("Thank you for using the temperature converter. Goodbye!")
        break
    
    if choice in ['1', '2']:
        temp = float(input("Enter the temperature: "))
        
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")
        else:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")
    else:
        print("Invalid choice. Please try again.")

    