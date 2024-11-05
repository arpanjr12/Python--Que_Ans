
# Write a function that accepts a string and returns the number of uppercase and lowercase letters.

def count(str):
    uppercase_count = 0
    lowercase_count = 0

    for c in str:
        if c.isupper():
            uppercase_count += 1
        elif c.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


str = "Hello World!"
upper, lower = count(str)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
