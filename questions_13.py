
# Write a program to reverse a string without using any built-in functions.

def reverce(string):   

    rev=string[::-1]    # [::-1] is not a function, but it is a **built-in feature of Python's
    return rev
   

string=str(input("enter the string: "))
print( reverce(string))




# def reverse(string):
#     rev = ""
#     for char in string:
#         rev = char + rev  
#     return rev

# string = input("Enter the string: ")
# print(reverse(string))
