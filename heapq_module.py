import heapq

"""
Heaps are data structures that satisfy the heap property:
Minheap - children of each node have to be equal or greater than the node
Maxheap - children of each node have to be equal or lesser than the node

Heaps can be used to implement a priority queue
A priority queue pops the highest priority element (lowest number)

To find the children of a specific node in a list visual of a heap:
i = node index
2*i+1 = first child
2*1+2 = second child
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