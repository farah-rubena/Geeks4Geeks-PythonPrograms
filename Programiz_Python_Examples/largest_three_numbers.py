'''WAPP to find the largest among 3 numbers'''

def largest_among_three(n1, n2, n3):

    if n1>n2 and n2>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
res = largest_among_three(n1=num1, n2=num2, n3=num3)
print(f"{res} is the highest among the three numbers")