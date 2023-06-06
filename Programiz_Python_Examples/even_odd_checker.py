'''WAPP to check whether a number is EVEN or ODD'''

def even_odd(num):

    if num%2 == 0:
        return f"{num} is an Even number"
    return f"{num} is an Odd number"


n = int(input("Enter a number: "))
print(even_odd(num=n))