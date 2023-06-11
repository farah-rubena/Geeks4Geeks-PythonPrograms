import calendar as cal

def calendar():

    y = int(input("Enter the year: "))
    m = int(input("Enter the month: "))
    print(cal.month(y, m))

calendar()
