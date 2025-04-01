def reverse_string(s):
    """Reverse the given string."""
    return s[::-1]

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Remove spaces and convert to lowercase for a more flexible check
    s = ''.join(s.split()).lower()
    return s == s[::-1]

def main():
    # Get input from user
    user_input = input("Enter a string: ")

    # Reverse the string
    reversed_string = reverse_string(user_input)
    print(f"Reversed string: {reversed_string}")

    # Check if it's a palindrome
    if is_palindrome(user_input):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")

if __name__ == "__main__":
    main()