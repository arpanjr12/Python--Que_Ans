
# Write a function to calculate the average of numbers in a list.

def avg(list):
    
    l= len(list)
    s=sum(list)
    return (s/l)

list=[1,7,5,2,4,9,3,8,6,10]

print(f"the average of number in a list is:{avg(list)}")