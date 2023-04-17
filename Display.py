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
            print("Email:", current_contact.email)
            print("------------------")
            current_contact = current_contact.next

    def add_contact(self, contact):
        # If the linked list is empty, set the new contact as the head
        if not self.head:
            self.head = contact
            return

        # Traverse the linked list and add the new contact at the end..
        current_contact = self.head
        while current_contact.next:
            current_contact = current_contact.next

        current_contact.next = contact

    def remove_contact(self, contact):
        # If the contact to be removed is the head, update the head :o
        if contact == self.head:
            self.head = contact.next
            return

        # Traverse the linked list and remove the contact
        predecessor = None
        current_contact = self.head
        while current_contact:
            if current_contact == contact:
                predecessor.next = current_contact.next
                return
            predecessor = current_contact
            current_contact = current_contact.next

    def search_contact(self, name):
        # Traverse the linked list and return the contact with the matching name *
        current_contact = self.head
        while current_contact:
            if current_contact.name == name:
                return current_contact
            current_contact = current_contact.next

        # If the contact is not found, return None :(
        return None
