# Importing the required module to read from the folder
import sys

# Importing a function to "listify" strings in a .txt file as integers
from load import load_numbers

numbers = load_numbers(sys.argv[1])