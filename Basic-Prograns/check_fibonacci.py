'''WAPP Python Program for How to check if a given number is Fibonacci number?
'''

def check_fibonacci(num):

    a = 0
    b = 1
    while b < num:
        temp = b
        b = a + b
        a = temp
    if b == num:
        return True
    else:
        return False
    
n = int(input("Enter the number: "))
if check_fibonacci(n):
    print(f"{n} is a Fibonacci Number")
else:
    print(f"{n} is not a Fibonacci Number")    
