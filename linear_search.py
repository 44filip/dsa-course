numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(_list, target):
    """
    Returns the index position of the target if found, else returns -1
    """
    
    for i in range(0, len(_list)):
        if _list[i] == target:
            return i
    return -1

def verify(index):
    if index != -1:
        print("Target found at index:", index)
    else:
        print("Target not found in list")
        

result = linear_search(numbers,5)
verify(result)

result = linear_search(numbers,11)
verify(result)