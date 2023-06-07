'''WAPP to find the factorial of a number'''

def factorial(num):

    res = 1
    for _ in range(1, num+1):
        res *=_
    return res

n = int(input("Enter a number: "))
print(factorial(num=n))