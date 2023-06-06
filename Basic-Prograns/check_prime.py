'''WAPP to chck whether a number is PRIME OR NOT 
Prime numbers are evenly divisible by 1 and itself'''

def check_prime(num):

    if num == 0 or num == 1:
        return "Not Prime"
    
    for i in range(2, int(num/2)+1):
        if num%i == 0:
            return f"{num} is Not Prime"
    return f"{num} is Prime"


n = int(input("Enter a number: "))
print(check_prime(num=n))