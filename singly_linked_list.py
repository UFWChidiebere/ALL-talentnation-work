class Node:
    def __init__(self, data):
        self.data = data      # Stores the actual information
        self.next = None      # Stores the reference to the next node (starts as None)

class LinkedList:
    def __init__(self):
        self.head = None      # The list starts empty, so head points to nothing

    # 1. Insert at the beginning: O(1) Time Complexity
    def insert_at_beginning(self, data):
        new_node = Node(data)         # Create the new node
        new_node.next = self.head     # Point the new node's clue to the current head
        self.head = new_node          # Make this new node the official new head

    # 2. Insert at the end: O(n) Time Complexity
    def insert_at_end(self, data):
        new_node = Node(data)
        
        # If the list is completely empty, this new node becomes the head
        if self.head is None:
            self.head = new_node
            return
        
        # Otherwise, start at the head and walk to the very last node
        current = self.head
        while current.next is not None:
            current = current.next  # Move to the next node
            
        # Now that we are at the last node, point its clue to our new node
        current.next = new_node

    # 3. Print the whole list (Traversal): O(n) Time Complexity
    def print_list(self):
        current = self.head
        
        # Walk through the list until we hit None (the end)
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Marks the end of the chain


# Create an empty linked list
my_chain = LinkedList()

# Add elements to the end
my_chain.insert_at_end("Node B")
my_chain.insert_at_end("Node C")

# Print the list to see what it looks like right now
print("Initial list:")
my_chain.print_list()
# Output: Node B -> Node C -> None

# Add an element to the absolute beginning
my_chain.insert_at_beginning("Node A")

print("\nAfter inserting at the beginning:")
my_chain.print_list()
# Output: Node A -> Node B -> Node C -> None
