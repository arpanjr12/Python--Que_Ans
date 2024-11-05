
# Write a function that takes a list of numbers and returns the sum of its elements.

def list(number):
    if not number:
         return 0
    
    total=sum(number)
    return total

number=[5,3,4,8,9,6,4,7]
total=list(number)

print(f"sum of it:",total)
