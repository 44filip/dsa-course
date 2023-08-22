#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - Code prior to importing

# Importing the required module to read from the folder
import sys

# Importing a function to "listify" strings in a .txt file as integers
from load import load_strings

names = load_strings(sys.argv[1])

def linear_search(_list, target):
    """
    Returns the index position of the target if found, else returns -1
    """
    
    for i in range(0, len(_list)):
        if _list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")
        

result = linear_search(names, "Michael Johnson")
verify(result)

result = linear_search(names, "Wrong Name")
verify(result)