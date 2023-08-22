# Importing the required modules to read from the folder and randomize values
import random
import sys

# Importing a function to "listify" strings in a .txt file as integers
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# Defining a O(n) function to check whether the list is sorted
def is_sorted(_list):

  for i in range(len(_list) - 1):
    if _list[i] > _list[i + 1]:
      return False
  return True

# Shuffling the values until the list is successfully sorted
def bogo_sort(_list):
    
    # Implementing a counter to see how many iterations it takes
    attempts = 0
    
    while not is_sorted(_list):
        attempts += 1
        print(attempts)
        random.shuffle(_list)
    return _list

print(bogo_sort(numbers))
