class HashTable:
    def __init__(self):
        # User Story 1: Initialize collection to an empty dictionary
        self.collection = {}

    def hash(self, string: str):
        # User Story 3 & 5: Sum the Unicode values of each character
        total = 0
        for char in string:
            total += ord(char)
        return total
    
    def add(self, key, value):
        # User Story 4: Compute the hash of the key
        hashed_key = self.hash(key)
        
        # If the hash index doesn't exist yet, create a nested dictionary there
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
            
        # Store the key-value pair inside the nested dictionary
        self.collection[hashed_key][key] = value

    def remove(self, key):
        # User Story 4: Compute the hash of the key
        hashed_key = self.hash(key)
        
        # Confirm if the hash index exists AND if the key is inside that nested dictionary
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            # Delete only the specific key-value pair
            del self.collection[hashed_key][key]

    def lookup(self, key):
        # User Story 4: Compute the hash of the key
        hashed_key = self.hash(key)
        
        # Check if the hash index exists AND if the key is inside that nested dictionary
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        
        # If the key does not exist, return None
        return None


# ========================================================
# PASTE THIS ENTIRE BLOCK AT THE BOTTOM OF YOUR CODE FILE
# ========================================================

# 1. Initialize the Hash Table (Build the empty warehouse)
print("--- 1. Building the empty Hash Table ---")
my_hash_table = HashTable()
print("Collection is empty:", my_hash_table.collection)  # Should print: {}
print()


# 2. Test the Hash Method (The ID Generator)
print("--- 2. Testing the Hash Generator ---")
golf_hash = my_hash_table.hash("golf")
print(f"The word 'golf' hashes to index: {golf_hash}")  # Should print: 424
print()


# 3. Test the Add Method (Adding a single item)
print("--- 3. Adding a single item ('golf') ---")
my_hash_table.add("golf", "sport")
print("Warehouse state:", my_hash_table.collection)  
# Should print: {424: {'golf': 'sport'}}
print()


# 4. Test Collision Resolution (Adding two items that share a shelf)
print("--- 4. Testing Collisions ('dear' and 'read') ---")
# Both 'dear' and 'read' contain the exact same letters, so they add up to 412
print(f"'dear' hashes to: {my_hash_table.hash('dear')}") # 412
print(f"'read' hashes to: {my_hash_table.hash('read')}") # 412

my_hash_table.add("dear", "friend")
my_hash_table.add("read", "book")
print("Warehouse state after collisions:")
print(my_hash_table.collection)
# Should print: {424: {'golf': 'sport'}, 412: {'dear': 'friend', 'read': 'book'}}
print()


# 5. Test Lookup Method (Finding items)
print("--- 5. Testing Lookups ---")
print("Looking up 'golf':", my_hash_table.lookup("golf"))    # Should print: sport
print("Looking up 'dear':", my_hash_table.lookup("dear"))    # Should print: friend
print("Looking up non-existent 'cfc':", my_hash_table.lookup("cfc"))  # Should print: None
print()


# 6. Test Remove Method (Safely discarding items)
print("--- 6. Testing Removals ---")
# Remove an item that shares a shelf ('dear') to ensure 'read' is safe
my_hash_table.remove("dear")
print("Warehouse state after removing 'dear':")
print(my_hash_table.collection)
# Should print: {424: {'golf': 'sport'}, 412: {'read': 'book'}}

# Try to remove something that doesn't exist (it should not crash the code)
my_hash_table.remove("fake_item")
print("Removing a non-existent item did not crash the system! ✅")
