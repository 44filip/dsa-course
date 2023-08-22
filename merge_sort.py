def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new, sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    
    Runs in O(n log n) /// O(kn log n) [splicing takes time (k) in Python]
    """
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list) 
    left = merge_sort(left_half)       # The recursive function is not async - it will fully divide, merge and sort the left side
    right = merge_sort(right_half)     # Then it will fully divide, merge and sort the right side
    
    return merge(left, right)          # At the end, merge and sort the two sorted lists

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Runs in overall O(log n) time /// O(k log n) [splicing takes time (k) in Python]
    """
    midpoint = len(list)//2       
    left = list[:midpoint]      
    right = list[midpoint:]     
    
    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new, merged list
    Runs in overall O(n) time
    """
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
            
    
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1
        
    return l
        
def verify_sorted(list):
    """
    Verifies the sorting of the list by recursively comparing values [0] and [1]
    Returns True or False accordingly
    """
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] <= list [1] and verify_sorted(list[1:]) # We use <= because it can be a duplicate


alist = [85, 53, 27, 17, 20, 90, 35]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))