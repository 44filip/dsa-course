numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def recursive_binary_search(_list, target):
    """
    A non iterative way to do a binary search
    Runs in O(log n)
    """
    if len(_list) == 0:
        return False
    else:
        midpoint = (len(_list))//2
        
        if _list[midpoint] == target:
            return True
        else:
            if _list[midpoint] < target:
                return recursive_binary_search(_list[midpoint+1:], target)
            else:
                return recursive_binary_search(_list[:midpoint], target)
            
def verify(result):
    print("Target found:", result)

result = recursive_binary_search(numbers, 3)
verify(result)