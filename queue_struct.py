class Queue:
    """
    Queues are a data structure of FIFO type (First-In-First-Out)
    Any item pushed into the list is added at the end
    Any item popped from the list is oldest addition (first element)
    The peek method returns the first element of the list (oldest addition)
    """
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
        
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    