class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added.")

    def edit_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact
                print(f"Contact {old_name} updated to {new_contact.name}.")
                return
        print(f"Contact {old_name} not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact {name} deleted.")
                return
        print(f"Contact {name} not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for contact in self.contacts:
                print(contact)

def main():
    phonebook = PhoneBook()

    while True:
        print("\n***PHONE BOOK APPLICATION***")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            phonebook.add_contact(contact)

        elif choice == '2':
            old_name = input("Enter the name of the contact to edit: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            new_contact = Contact(name, phone, email)
            phonebook.edit_contact(old_name, new_contact)

        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            phonebook.delete_contact(name)

        elif choice == '4':
            phonebook.display_contacts()

        elif choice == '5':
            print("Exiting the Phone Book Application....")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
