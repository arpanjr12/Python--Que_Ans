

# Write a function that takes a list of numbers and returns a list with unique elements (remove duplicates).

def uniques(numbers):
    
    return list(set(numbers))      # Use a set to remove duplicates, then convert back to a list


numbers = [5,3,9,5,4,6,2,1,8,7,4,8,3,2,7,9,5,0,1,0,6,0]
list = uniques(numbers)
print("Unique elements:", list)
