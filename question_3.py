
 # Write a program to check if a given word is a palindrome.

# Ask the user for a number
# number = input("Enter a number: ")


# if number == number[::-1]: #The [::-1] is a slice notation in Python. It means "take the string and step backwards from the end to the start."In other words, it reverses the string.
#     print(f"{number} is a palindrome number.")
# else:
#     print(f"{number} is not a palindrome number.")

  
user_input =str(input("Enter a word or number: ")) # 'str' use for convert input into string for both number and word

def palindrome(user_input):      
    return user_input == user_input[::-1]

if palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")    
else:
    print(f"'{user_input}' is not a palindrome.")
