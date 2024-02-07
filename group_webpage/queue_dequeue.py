class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def append_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop_front(self):
        if self.is_empty():
            raise Exception("List is empty, cannot pop front")
        data = self.head.data
        self.head = self.head.next
        return data
    
    def pop_back(self):
        if self.is_empty():
            raise Exception("List is empty, cannot pop back")
        
        # If there is only one node in the list
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        data = current.next.data
        current.next = None
        return data

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        elements.append("")
        return " -> ".join(elements)

class Queue_Deque():
    def __init__(self):
        self.Queue_Deque = LinkedList()

    def push_front(self, data):
        self.Queue_Deque.append_head(data)

    def push_back(self, data):
        self.Queue_Deque.append(data)

    def pop_front(self):
        if self.Queue_Deque.is_empty():
            return None
        return self.Queue_Deque.pop_front()

    def pop_back(self):
        if self.Queue_Deque.is_empty():
            return None
        return self.Queue_Deque.pop_back()

    def get_elements(self):
        return self.Queue_Deque.display()
        

