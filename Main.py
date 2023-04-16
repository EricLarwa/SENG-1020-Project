from Display import Contact

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("No contact found")
        #FIXme (Continue)

    def add_contact(self, name, phone, email):
          #FIXme

    def remove_contact(self, contact):
        successor = contact.next
        predecessor = contact.prev
        if successor != None:
            successor.prev = predecessor
        if predecessor != None:
            predecessor.next = successor
        if contact is self.head:
            self.head = successor
        if contact is self.tail:
            self.tail = predecessor

    def search_contact(self, search_contact):
        current_contact = self.head
        while current_contact != None:
            if current_contact == search_contact:
                return current_contact
            else:
                current_contact = current_contact.next

        return None

Contact_Book = LinkedList()
while True:
    print("Enter 1 to add a new contact")
    print("Enter 2 to display all contacts")
    print("Enter 3 to search contacts")

    choice = int(input("Enter your choice:"))
    print("                                ")
    if choice == 1:
        name = input("Enter the name:")
        phone = input("Enter phone number:")
        email = input("Enter the email address:")
        contact = Contact(name,phone,email)
        Contact_Book.add_contact(contact)
        print("Contact added",'\n')
    elif choice == 2:
        Contact_Book.display()
    elif choice == 3:
        print("Exiting...")
        break
    else:
         print("Invalid choice")