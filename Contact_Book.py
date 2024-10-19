import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    
    name = input("Enter the contact name: ")
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

def view_contact(contacts):
    
    name = input("Enter the contact name: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found.")

def update_contact(contacts):
    
    name = input("Enter the contact name to update: ")
    if name in contacts:
        print(f"Current details: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        phone = input("Enter new phone number (leave blank to keep current): ") or contacts[name]['phone']
        email = input("Enter new email address (leave blank to keep current): ") or contacts[name]['email']
        
        contacts[name] = {
            'phone': phone,
            'email': email
        }
        save_contacts(contacts)
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts):
    
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ").lower()
        if confirm == 'yes':
            del contacts[name]
            save_contacts(contacts)
            print(f"Contact {name} deleted successfully!")
        else:
            print("Deletion canceled.")
    else:
        print(f"Contact {name} not found.")

def list_contacts(contacts):
    
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")

def contact_book():
    
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    contact_book()
