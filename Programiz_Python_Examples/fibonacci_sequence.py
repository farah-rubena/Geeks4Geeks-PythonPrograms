'''WAPP to write the Fibonacci Sequence
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

'''


def fibonacci_seq(terms):

    if terms <=0:
        return "Invalid Input"
    elif terms == 0:
        return 1
    elif terms == 1:
        return 2
    else:
        prev1 = 0
        prev2 = 1
        for _ in range(3, terms+1):            
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
            print(curr)

n = int(input("How many terms?: "))
fibonacci_seq(terms=n)
