class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node
    """
    data = None
    next_node = None
    prev_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
    
class LinkedList:
    """
    Doubly linked list (DLL)
    """
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        """
        Returns a string representation of the list
        Runs in O(n) time
        """
        nodes = []
        current = self.head
        
        while current is not None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
                
            current = current.next_node
        return '-> '.join(nodes)
        
    def append(self, data):
        """
        Adds a new Node containing data at the head of the list
        Runs in overall O(n) time
        """
        new_node = Node(data)
        current = self.head
        
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node
            new_node.prev_node = current
            new_node.next_node = None

    def prepend(self, data):
        """
        Adds a new Node containing data at the head of the list
        Runs in O(1) time
        """
        new_node = Node(data)
        
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            new_node.next_node = self.head
            new_node.prev_node = None
            self.head.prev_node = new_node
            self.head = new_node
        
    def is_empty(self):
        return self.head is None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Runs in O(n) time
        """
        current = self.head
        count = 0
        
        while current is not None:
            count += 1
            current = current.next_node
            
        return count