'''WAPP to check if a number is positive, negative or zero'''

def number_checker(num):

    if num < 0: 
        return "Negative"
    elif num > 0:
        return "Positive" 
    else:
        return "Zero"

n = int(input("Enter a number: "))
print(number_checker(num=n))