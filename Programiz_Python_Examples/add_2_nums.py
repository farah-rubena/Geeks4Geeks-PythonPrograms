'''WAPP to add two numbers'''

#Solution 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(num1+num2)

#Solutuon 2

def add_nums(num1, num2):
    return num1 + num2

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(add_nums(num1=n1, num2=n2))