
# Create a program that converts temperature from Celsius to Fahrenheit and vice versa.

#  rules=> c/5 = (f-32)/9
#             c= 5*((f-32)/9)
#             f=(9*c+160)/5



def convert(temp):

    fahrenheit=round((9*temp+160)/5)  #round() to ensure the output is a whole number.
    celsius=5*((temp-32)/9)
    return fahrenheit,celsius

temp=int(input("enter temprature: "))
fahrenheit,celsius=convert(temp)
print(f" Fahrenheitis to celsius is:  {celsius}")
print(f"celsius to Fahrenheitis is:  {fahrenheit}")