class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.email = email
        self.phone = phone
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("No contacts found.", '\n')
            return

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

    def remove_contact(self, name):
        if self.head is None:
            print(f"{name} was not found")
            return

        if self.head.name == name:
            self.head = self.head.next
            print(f"{name} has been removed from the contact book", '\n')
            return

        successor = self.head
        predecessor = None
        while successor.next != None:
            if successor.name == name:
                if predecessor != None:
                    predecessor.next = successor.next
                else:
                    self.head = successor.next
                print(f"{name} has been removed from the contact book.", '\n')
                return
            predecessor = successor
            successor = successor.next
        print(f"{name} is not in the contact book.", '\n')

    def search_contact(self, name):
        current_contact = self.head
        while current_contact is not None:
            if current_contact.name == name:
                print(f"Here is the contact information for {name}: ")
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
        print("The Contacts have been sorted by name", '\n')
