contact = {}

def display_contact():
    if not contact:
        print("No contacts available.")
    else:
        print("\nYour Contacts:")
        for name, phone in contact.items():
            print(f"{name}: {phone}")

while True:
    choice = int(input("1. Add Contact\n2. View Contact\n3. Display Contacts\n4. Edit Contact\n5. Delete Contact\nEnter your choice 1-5: "))
    
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact[name] = phone
        print("Contact added successfully.")
        display_contact()
        
    elif choice == 2:
        search_name = input("Enter name to search: ")
        if search_name in contact:
            print(f"{search_name}: {contact[search_name]}")
        else:
            print(f"No contact found for {search_name}.")
        display_contact()
        
    elif choice == 3:
        if not contact:
            print("No contacts to display.")
        else:
            display_contact()
        
    elif choice == 4:
        edit_contact = input("Enter name to edit: ")
        if edit_contact in contact:
            new_phone = input("Enter new phone number: ")
            contact[edit_contact] = new_phone
            print("Contact updated successfully.")
        else:
            print("Name not found.")
        display_contact()
        
    elif choice == 5:
        del_contact = input("Enter name to delete: ")
        if del_contact in contact:
            confirm = input(f"Are you sure you want to delete {del_contact}? (yes/no): ")
            if confirm.lower() == "yes":
                contact.pop(del_contact)
                print("Contact deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Name not found.")
        display_contact()
