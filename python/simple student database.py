import csv

def add_student(filename):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])
    print("Student added successfully.")

def view_students(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Name: {row[0]}, Age: {row[1]}, Grade: {row[2]}")
    except FileNotFoundError:
        print("No students found. Database is empty.")

def delete_student(filename):
    name = input("Enter the name of the student to delete: ")
    temp_list = []
    deleted = False
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                temp_list.append(row)
            else:
                deleted = True
    
    if deleted:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(temp_list)
        print(f"Student {name} deleted successfully.")
    else:
        print(f"Student {name} not found.")
def main():
    filename = 'students.csv'
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student(filename)
        elif choice == '2':
            view_students(filename)
        elif choice == '3':
            delete_student(filename)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()