new_list = [1, 2, 3]
numbers = []
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        
        break
    
numbers.append(1)         # Add at the end
numbers.insert(1, 2)      # Add at specific position, shift everything else
numbers.extend([3, 4, 5]) # Add entire list at the end

numbers.pop(0)            # Removes at index 0
numbers.pop()             # Removes the last element
numbers.remove(4)         # Removes specific element
numbers.clear()           # Clears list to []

numbers.append("success")

