
# Create a function that takes two numbers and returns their sum, difference, product, and quotient.

def task(num1,num2):
    sum= num1+num2
    difference= num1-num2   
    product=num1*num2   
    if(num2 !=0):
      quotient=num1/num2      
    else:
       quotient = "Undefined (division by zero)"

    return sum,difference,product,quotient


num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
reasult= task(num1,num2)


print(f"sum:{reasult[0]}")
print(f"difference:{reasult[1]}")
print(f"product:{reasult[2]}")
print(f"quotient:{reasult[3]}")


   
     
