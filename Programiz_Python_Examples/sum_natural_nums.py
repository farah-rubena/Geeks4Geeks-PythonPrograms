'''WAPP to find the sum of natural numbers'''

def natural_num_sum(n):

    if n < 1:
        return "Enter a positive number: "
    else:
        sum = 0
        for _ in range(n+1):
            sum += _
        return sum


num = int(input("Enter the number: "))
res = natural_num_sum(n=num)
print(res)