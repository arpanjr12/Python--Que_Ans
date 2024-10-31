
# Write a function to find the largest and smallest numbers in a list.

def list(numbers):
    if not numbers:
        return None, None  
        
    largest = max(numbers)
    smallest = min(numbers)
    
    return largest, smallest


numbers =[1,2,5,4,8,6]
largest, smallest = list(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)

    