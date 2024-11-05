
# Make a function that returns True if a given year is a leap year and False otherwise.

def leap(year):
    # A year is a leap year if it's divisible by 4
    # But years divisible by 100 are not leap years unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
print(leap(year))
