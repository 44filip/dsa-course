# Importing the required module to read from the folder
import sys

# Importing a function to "listify" strings in a .txt file as integers
from load import load_strings

names = load_strings(sys.argv[1])

def quicksort(_list):
    """
    Runs in O(n^2) worst case                   [Pivot is the smallest or the largest number]
    Runs in O(n log n) best case                [Pivot is a median value of the list]
    Runs in O(n log n) average case             [Getting the worst/best case is rare]
    """
    if len(_list) <= 1:                         # Set up a base case which stops the recursion
        return _list
    
    less_than_pivot = []                        # Initialize lesser list as an empty list
    greater_than_pivot = []                     # Initialize greater list as an empty list
    pivot = _list[0]                            # Set pivot as the element at index 0 (first element)
    for element in _list[1:]:                   # Iterate every element excluding the pivot
        if element <= pivot:                    # If the element is lesser, add it to the less_than list
            less_than_pivot.append(element)
        else:
            greater_than_pivot.append(element)  # If the element is greater, add it to the greater_than list
            
            """
            Quicksorts the list and all its sublists in a stack until it reaches the base case
            When the base case is met, the stack unveils, and the values are sorted
            The end values are then added before and after the pivot respectively
            """
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
            
    
sorted_names = quicksort(names)
for n in sorted_names:
    print (n)