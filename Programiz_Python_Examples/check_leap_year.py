'''WAPP to check whether a year is a leap year or not
A year is a leap year if it is evenly divisible by 4.
However, if the year is also divisible by 100, it is not a leap year, unless...
If the year is divisible by 400, then it is a leap year.
'''

def check_leap(year):

    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return f"{year} Is Leap"
            else:
                return f"{year} is Not Leap"
        else:
            return f"{year} Is Leap"
    else:
        return f"{year} is Not Leap"


y = int(input("Enter the year: "))
print(check_leap(year=y))