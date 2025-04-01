def get_student_data():
    students = {}
    while True:
        name = input("Enter student name (or press Enter to finish): ")
        if name == "":
            break
        
        while True:
            try:
                score = float(input(f"Enter score for {name}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric score.")
        
        students[name] = score
    return students

def highest_score(students):
    return max(students.values())

def average_score(students):
    return sum(students.values()) / len(students)

def names_alphabetical(students):
    return sorted(students.keys())

def main():
    print("Enter student names and scores:")
    students = get_student_data()
    
    if not students:
        print("No student data entered.")
        return
    
    print("\nResults:")
    print(f"Highest score: {highest_score(students)}")
    print(f"Average score: {average_score(students):.2f}")
    print("Names in alphabetical order:")
    for name in names_alphabetical(students):
        print(name)

if __name__ == "__main__":
    main()