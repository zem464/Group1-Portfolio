class HashTable:
    def __init__(self, size=32):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.deleted_items = []

    # Hash function 1
    def hash_function_1(self, key):
        return key % self.size

    # Hash function 2
    def hash_function_2(self, key):
        return ((1731 * key + 520123) % 524287) % self.size
    
    def hash_function_3(self, key):
        return hash(key) % self.size

    def insert(self, key, function):
        if ',' in key:
            keys = key.split(', ')
        else:
            keys = [key]

        for k in keys:
            k_str = str(k)  # Convert the key to a string
            if function == "Division":
                hashed_key = self.hash_function_1(k_str)
                self.table[hashed_key].insert(0, k_str)
            elif function == "Multi":
                hashed_key = self.hash_function_2(k_str)
                self.table[hashed_key].insert(0, k_str)
            elif function == "Default":
                hashed_key = self.hash_function_3(k_str)
                self.table[hashed_key].insert(0, k_str)

    def delete(self, keys):
        for i, slot in enumerate(self.table):
            if keys in slot:
                slot.remove(keys)
                self.deleted_items.append(f"Deleted: {keys}")
                return
        self.deleted_items.append(f"Key not found: {keys}")

    def display(self):
        result = []

        for i, slot in enumerate(self.table):
            # Filter out items with 'del' in the slot
            slot = [item for item in slot if 'del' not in item]
            values = ' '.join(slot)
            result.append(f"{i}: {values}")

        # Display deleted items separately
        if self.deleted_items == 'del ':
            result.append("Deleted Items:")
            for item in self.deleted_items:
                result.append(item)

        return result

    def process_command(self, command, hash_function):
        for cmd in command:
            if cmd.startswith("del "):
                word_to_delete = cmd[4:]
                key = sum(ord(char) for char in word_to_delete)
                index = hash_function(key)
                if word_to_delete in self.table[index]:
                    self.table[index].remove(word_to_delete)
                    self.deleted_items.append(f"Deleted: {word_to_delete}")
            else:
                key = sum(ord(char) for char in cmd)
                index = hash_function(key)
                self.table[index].insert(0, cmd)
