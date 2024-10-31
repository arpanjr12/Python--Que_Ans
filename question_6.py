
# Generate the first n numbers in the Fibonacci sequence.

def fibo(n):
    if (n<=1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)
            
n=int(input("enter the number: "))

print(fibo(n))