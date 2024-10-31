
# Create a simple calculator that takes user input for two numbers and an operator (+, -, *, /) and prints the result.


num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':   
   if num2 == 0:
        result = "Error: Division by zero is not allowed."
   else:
        result = num1 / num2

else:
    result = "Error: Invalid operator."


print("Result:", result)



