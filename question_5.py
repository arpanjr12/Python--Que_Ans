
# Write a function that calculates the factorial of a given number.


def factorial(n):
        if(n==0 or n==1):
            return 1
        
        else:      
            return n*factorial(n-1)    
     
n=int(input("enter the number: "))
print(factorial(n))