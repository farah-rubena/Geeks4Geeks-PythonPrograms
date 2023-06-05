'''WAP to get the factorial of a number
Factorial is written as n!
To find the factorial of a number we multiply it by all the numbers that come before it'''

#SOLUTUON ONE
factorial_num = int(input("Enter the number you wan to find the factorial of: "))

result = 1

for n in range(1, factorial_num + 1):
    result = result * n
print(result)


#SOLUTUON TWO
def find_factorial(num):

    res = 1
    for n in range(1, num+1):
        res *= n
    return res

n = int(input("Enter a number: "))
print(find_factorial(num=n))


#SOLUTION 3
import math
def num_factorial(num):
    
    return math.factorial(num)

n = int(input("Enter a number: "))
print(num_factorial(num=n))
