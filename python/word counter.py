def analyze_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.split('\n')
        words = content.split()
        characters = len(content)
        
    print(f"Number of lines: {len(lines)}")
    print(f"Number of words: {len(words)}")
    print(f"Number of characters: {characters}")

# Example usage
analyze_file('C:/Users/Ayogaius/Documents/OUTPUT.doc')  # Replace with your file name