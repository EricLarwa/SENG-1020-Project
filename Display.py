class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.email = email
        self.phone = phone
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        # If no contacts exist, print a message and return :P
        if not self.head:
            print("No contacts found.")
            return

        # Traverse the linked list and print the details of each contact **
        current_contact = self.head
        while current_contact:
            print("Name:", current_contact.name)
            print("Phone:", current_contact.phone)
            print("Email:", current_contact.email, '\n')

            current_contact = current_contact.next

    def add_contact(self, contact):
        if not self.head:
            self.head = contact
            return

        current_contact = self.head
        while current_contact.next is not None:
            current_contact = current_contact.next
        current_contact.next = contact

    def remove_contact(self, contact):
        if self.head is None:
            print(f"{contact} was not found")
            return

        successor = contact.next
        predecessor = contact.prev
        while successor is not None:
            if successor != None:
                successor.prev = predecessor
            if predecessor != None:
                predecessor.next = successor
            if contact is self.head:
                self.head = successor

    def search_contact(self, name):
        current_contact = self.head
        while current_contact is not None:
            if current_contact.name == name:
                print(f"{name} ")
                print(f"{current_contact.phone} ")
                print(f"{current_contact.email}",'\n')
                return
            current_contact = current_contact.next
        print(f"{name} is not in the Contact Book")
    def sort_list(self):
        if self.head is None:
            print("The Contact Book Is Empty")
        current = self.head
        contact_list = []
        while current is not None:
            contact_list.append(current)
            current = current.next

        sorted_list = sorted(contact_list, key=lambda x: x.name)
        self.head = sorted_list[0]
        current = self.head
        for contact in sorted_list[1:]:
            current.next = contact
            current = current.next
        current.next = None
        print("The Contacts have been sorted by name")
