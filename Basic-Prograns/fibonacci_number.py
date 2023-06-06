'''A Fibonacci number is a sequence of numbers in which each number is the sum of the two preceding numbers. The sequence starts with 0 and 1
WAPP for the n-th fibinacci number'''


def fibonacci(num):
    #check if the number is ina  valid range
    if num<=0:
        return "Invalid Input"
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        prev1 = 0
        prev2 = 1
        for _ in range(3, n+1):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
        return curr
    
n = int(input("Enter a number: "))
print(f"The {n}-th Fibonacci number is: {fibonacci(num=n)}")
