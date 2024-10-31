
# Write a program that counts the frequency of each character in a string.


def count(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


string = str(input("enter your string: "))
print(count(string))
