
# Create a program that asks the user for a number and returns its multiplication table.

n=int(input('enter your  number: '))

for i in range(1,21):
    print(f"{n}x{i} = {n*i}")
