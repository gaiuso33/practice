def print_multiplication_table(n):
    print(f"Multiplication table up to {n}x{n}:")
    
    # Print header row
    print("   |", end='')
    for i in range(1, n + 1):
        print(f"{i:3}", end='')
    print("\n---+" + "---" * n)
    
    # Print table content
    for i in range(1, n + 1):
        print(f"{i:2} |", end='')
        for j in range(1, n + 1):
            print(f"{i*j:3}", end='')
        print()  # Newline after each row

# Get user input
size = int(input("Enter the size of the multiplication table: "))
print_multiplication_table(size)