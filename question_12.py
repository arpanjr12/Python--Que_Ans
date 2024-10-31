
# Create a function that finds all the prime numbers up to a given number.

def check(n):
    
    for i in range(2, n + 1):
        for number in primes:
            if i % number == 0:
                break
        else:
            primes.append(i)
    return primes

primes = []
print(check(30))  