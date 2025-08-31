contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(" Contact added!")

def view_contacts():
    if not contacts:
        print(" No contacts found.")
    else:
        print("\n Contact List:")
        for name, phone in contacts.items():
            print(f" {name} :  {phone}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(" Contact deleted.")
    else:
        print(" Contact not found.")


while True:
    print("\n CONTACT BOOK MENU")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        print(" goodbye!")
        break
    else:
        print(" Invalid option. Try again.")
