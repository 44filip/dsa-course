#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - Code prior to importing

# Importing the required module to read from the folder
import sys

# Importing a function to "listify" strings in a .txt file as integers
from load import load_strings

names = load_strings(sys.argv[1])

def binary_search(_list, target):
    first = 0
    last = len(_list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if _list[midpoint].lower() == target.lower():
            return midpoint
        elif _list[midpoint].lower() < target.lower():
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(found_index):
    if found_index:
        print("Target found at index:", found_index)
    else:
        print("Target not found in list")
        
result = binary_search(names, "Michael Johnson")
verify(result)

result = binary_search(names, "Wrong Name")
verify(result)