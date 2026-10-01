class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at first
    def insert_first(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Insert at last
    def insert_last(self, data):
        new_node = Node(data)

        # If linked list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        # Move to the last node
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Display linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Create linked list
ll = LinkedList()

# User input
n = int(input("Enter number of elements: "))

for i in range(n):
    data = int(input("Enter value: "))
    ll.insert_last(data)

print("\nOriginal Linked List:")
ll.display()

# Insert at first
value = int(input("\nEnter value to insert at first: "))
ll.insert_first(value)

print("After inserting at first:")
ll.display()

# Insert at last
value = int(input("\nEnter value to insert at last: "))
ll.insert_last(value)

print("After inserting at last:")
ll.display()