class Node:
    """
    An object for storing a single node of a tree
    Models two attributes - data and the list of children
    """
    data = None
    
    def __init__(self, data):
        self.data = data
        self.children = []
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, root):
        self.root = root
        

"""
Preorder, inorder and postorder are all DEPTH-FIRST (Stack)
"""

def preorder(node):
    # Runs in O(n)
    if node is None:
        return
    
    print(node.data)
    preorder(node.left)
    preorder(node.right)
    
        
def inorder(node):
    # Runs in O(n)
    if node is None:
        return
    
    inorder(node.left)
    print(node.data)
    inorder(node.right)
    
def postorder(node):
    # Runs in O(n)
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)


"""
Levelorder is BREADTH-FIRST (Queue)
"""

def levelorder(node):
    # Runs in O(n)
    if node is None:
        return

    queue = [node]
    while queue:
        popped = queue.pop(0)
        print(popped.data)

        if popped.left is not None:
            queue.append(popped.left)
        if popped.right is not None:
            queue.append(popped.right)
        
        
        
root = Node(1)

left_child = Node(2)
root.left = left_child

right_child = Node(3)
root.right = right_child
root.children = [left_child, right_child]

left_child.left = Node(4)
left_child.right = Node(5)
right_child.left = Node(6)
right_child.right = Node(7)

tree = Tree(root)

print("Preorder")
preorder(tree.root)
print("Inorder")
inorder(tree.root)
print("Postorder")
postorder(tree.root)
print("Levelorder")
levelorder(tree.root)

