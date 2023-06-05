#WAP to get the MAXIMUM of two numbers

#SOLUTION ONE
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{max(num1, num2)} is the bigger number")


#SOLUTION TWO
def max_num(a, b):

    if a>b:
        return a
    return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(max_num(a,b))


#SOLTUON 3
maximum  = lambda a,b: a if a>b else b
print(maximum(2,8))


#SOLUTON 4
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
x = [a,b]
x.sort()
print(x[-1])