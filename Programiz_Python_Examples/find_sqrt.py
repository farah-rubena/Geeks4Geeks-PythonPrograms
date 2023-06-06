'''WAPP to find the sqrt

The square root of a number is a value that, when multiplied by itself, gives the original number. It is denoted by the symbol "√".

For example, the square root of 25 is 5 because 5 multiplied by itself equals 25: √25 = 5.

'''

#Solution 1
num = int(input("Enter the number: "))
sqrt = num**0.5
print(f"The sqrt of {num} is {sqrt:.2f}" )

#Solution 2
def num_sqrt(num):
    return num**0.5

n = int(input("Enter the number: "))
print(num_sqrt(num=n))