class Stack:
    """
    Stacks are a data structure of LIFO type (Last-In-First-Out)
    Any item pushed into the list is added at the end
    Any item popped from the list is the most recently added one
    The peek method returns the last element of the list (most recently added)
    """
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0