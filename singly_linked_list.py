class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node
    """
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
    
class LinkedList:
    """
    Singly linked list (SLL)
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
    
    def node_index(self, index):
        
        if index == 0:
            return self.head
        else:
            current = self.head
            position = index
            
            while position > 0:
                current = current.next_node
                position -= 1
                
            return current
            
    
    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        Runs in O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def insert(self, data, index): # Faux index, these are unindexed elements
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node takes O(n) time
        Returns the node's data and index at which it was inserted
        Runs in overall O(n) time
        """
        list_size = self.size()
        
        if index < 0 or index > list_size:
            raise IndexError("Index out of bounds")
        elif index == 0:
            self.add(data)
        elif index > 0:
            new = Node(data)
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1
                
            prev_node = current
            next_node = current.next_node
        
            prev_node.next_node = new
            new.next_node = next_node
            
        return "<Inserted %s at index %s>" % (data, index)
        
    def remove(self,key):
        
        """
        Removes Node containing data that matches the key
        Returns the removed node's data or None
        Runs in O(n) time
        """
        current = self.head
        prev_node = None
        found = False
            
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
                # The current pointer is updated to point to the next node
                # When an object becomes unreachable it is eligible for automatic garbage collection
            elif current.data == key:
                found = True
                prev_node.next_node = current.next_node
            else:
                prev_node = current
                current = current.next_node
            
        if found:
            return "Removed node with data: %s" % key
        else:
            return None
    
    def remove_index(self,index): # Faux index, these are unindexed elements
        """
        Removes Node at specified index
        Returns the removed node's index or None
        Runs in O(n) time
        """
        current = self.head
        prev_node = None
        list_size = self.size()
        
        if index < 0 or index > list_size:
            raise IndexError("Index out of bounds")
        elif index == 0:
            self.head = current.next_node
        elif index > 0:
            position = index
            
            while position > 0:
                prev_node = current
                current = current.next_node
                position -= 1
                
            prev_node.next_node = current.next_node
        
        return "<Removed node at index %s>" % index
            
                
        
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or None
        Runs in O(n) time
        """
        
        current = self.head
        
        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
                
        return None