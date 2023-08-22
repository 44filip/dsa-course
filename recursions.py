def sum(numbers):
    
    if not numbers:                         # While the list (or sublists) aren't empty, it keeps iterating
        return 0                            # When it reaches an empty list, returns the value 0
    
    remaining_sum = (sum(numbers[1:]))      # Makes a sum "stack" until reaching an empty list
    return numbers[0] + remaining_sum       # When the stack is unveiled, returns the total sum

alist = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(sum(alist))
     