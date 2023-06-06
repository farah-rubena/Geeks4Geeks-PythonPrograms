'''WAPP to check if a number is Prime
A number is Prime is it only positive divisors are 1 and itself'''


def prime_checker(num):

    if num < 2:
        return "Not Prime"
    
    for _ in range(2, int(num/2)+1):
        if num%_ == 0:
            return f"{num} is Not Prime"
    else:
        return f"{num} is Prime"
    
n = int(input("Enter the number to be checked: "))
res = prime_checker(num=n)
print(res)