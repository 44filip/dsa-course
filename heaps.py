import heapq

"""
Heaps are data structures that satisfy the heap property:
Minheap - children of each node have to be equal or greater than the node
Maxheap - children of each node have to be equal or lesser than the node

Heaps can be used to implement a priority queue
A priority queue pops the highest priority element (lowest number)
"""

def flipList(_list):
    _list = [-i for i in _list]
    
    return _list


data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
flip = flipList(data)

# All of these are minheaps
print("Original data: \n%s\n" % data)
heapq.heapify(data)
print("Heapified data: \n%s\n" % data)
heapq.heappop(data)
print("Heappopped data: \n%s\n" % data)
heapq.heappush(data, 2)
print("Heappushed data (2): \n%s\n" % data)

# Flipping the list makes it a maxheap
print("Original data: \n%s\n" % flip)
heapq.heapify(flip)
print("Heapified data: \n%s\n" % flip)
heapq.heappop(flip)
print("Heappopped data: \n%s\n" % flip)
heapq.heappush(flip, -2)
print("Heappushed data (-2): \n%s\n" % flip)


# Merged AND heapified two lists
l1 = [10, 20, 30, 40, 50]
l2 = [15, 25, 35, 45, 55]
l3 = heapq.merge(l1,l2)
# The result is a generator, hence we must use list
# Generators are functions that give one value at a time
print("Heapmerged data (l1 & l2): \n%s\n" % list(l3))


# To find the specific nodes from a heap in list form follow the code below
def left_child(i):
    return 2*i

def right_child(i):
    return 2*i + 1

def parent(i):
    return i//2
# End of code snippet for locating nodes


def max_heapify(a, heap_size, i):
    """
    Runs in O(log n)
    """
    l = left_child(i)
    r = right_child(i)

    largest = i 

    # Compare left child with target node
    if l < heap_size and a[l] > a[i]:
    # If the left child is greater, assign it the pointer
        largest = l
    
    # Compare right child with target node (or left child (step above))
    if r < heap_size and a[r] > a[largest]:
    # If the right child is greater, assign it the pointer
        largest = r 
    
    # If the pointer isn't at the target node
    if largest != i:
        # Swap the elements to fix it
        a[i], a[largest] = a[largest], a[i]
        # Then recursively max_heapify the children
        max_heapify(a, heap_size, largest)


def build_max_heap(_list):
    heap_size = len(_list)

    # This part confuses me, will try to understand later
    for i in range(heap_size//2, -1, -1):
        max_heapify(_list, heap_size, i)
        
build_max_heap(data)
print("Maxheapified data: \n%s\n" % data)