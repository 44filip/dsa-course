# Importing the required module to read from the folder
import sys

# Importing a function to "listify" strings in a .txt file as integers
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(_list):
    """
    Runs in O(n^2)
    """
    sorted_list = []                                         # Initialize an empty list
    for i in range(len(_list)):                             # Iterate as many times as there are elements in the list
        index_to_move = index_of_min(_list)                 # Find the index of the smallest element (expanded in index_of_min)
        sorted_list.append(_list.pop(index_to_move))        # Pop and append the selected element to the sorted list
    return sorted_list                                       # Once done, return the sorted list

def index_of_min(_list):
    min_index = 0                                            # Theoretically, the first index seen is the smallest
    for i in range(1, len(_list)):                          # Iterate as many times as there are elements, excluding index 0
        if _list[i] < _list[min_index]:                    # If the current index's value is less than the observed minimum
            min_index = i                                    # Mark its' index as the min_index, and iterate again
    return min_index                                         # Return the smallest number's index

print(selection_sort(numbers))