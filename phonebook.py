# Step 2: Initialize the Phonebook
phonebook = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        print("Contact already exists!")
    else:
        phone = input("Enter contact phone number: ")
        phonebook[name] = phone
        print(f"Contact {name} added successfully!")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in phonebook:
        print(f"Phone number of {name}: {phonebook[name]}")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def list_contacts():
    if phonebook:
        print("Phonebook Entries:")
        for name, phone in phonebook.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("Phonebook is empty.")

# Step 3: User Interface
def main():
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add a New Contact")
        print("2. Search for a Contact")
        print("3. Delete a Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        # Step 4: Implementing CRUD Operations
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Exiting Phonebook application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Step 1: Setup the Project
if __name__ == "__main__":
    main()
