from Display import Contact
from Display import LinkedList


Contact_Book = LinkedList()
while True:
    print("Enter 1 to Add a new Contact")
    print("Enter 2 to Display all Contacts")
    print("Enter 3 to Search Contacts")
    print("Enter 4 to Remove a Contact")
    print("Enter 5 to Sort Contacts")
    print("Enter 6 to Exit")

    choice = int(input("Enter your choice:"))
    print("                                ")
    if choice == 1:
        name = input("Enter the name: ")
        phone = input("Enter phone number: ")
        email = input("Enter the email address: ")
        contact = Contact(name,phone,email)
        Contact_Book.add_contact(contact)
        print("Contact added",'\n')
    elif choice == 2:
        Contact_Book.display()
    elif choice == 3:
        name = input("Enter the name of the contact you are searching for: ")
        print("                         ")
        Contact_Book.search_contact(name)
    elif choice == 4:
        name = input("Enter the name of the contact to be removed: ")
        print("                         ")
        Contact_Book.remove_contact(contact)
    elif choice == 5:
        Contact_Book.sort_list()
    elif choice == 6:
        print("Exiting...")
        break
    else:
         print("Invalid choice")