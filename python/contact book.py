def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")
def view_contact(contacts):
    name = input("Enter the name of the contact you want to view: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found!")
def update_contact(contacts):
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        phone = input("Enter the new phone number (press enter to skip): ")
        email = input("Enter the new email (press enter to skip): ")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found!")
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found!")
def list_contacts(contacts):
    if contacts:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact book is empty!")
def main():
    contacts = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. View a contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. List all contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            list_contacts(contacts)
        elif choice == '6':
            print("Thank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()