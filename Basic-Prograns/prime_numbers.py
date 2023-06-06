'''WAPP to print all prime numbers in an interval between two numbers
Prime Nos : Numbers greater than 1 that are only divisible by 1 and itself. Have only 2 positive divisors
 if a number is not divisible by any number smaller than half of itself, then it won't be divisible by any larger number either.
'''
def find_prime(num1, num2):


    prime_list = []

    #check if the number is less than 2
    for i in range(num1, num2):
        if i == 0 or i == 1:
            continue
        for j in range(2, int(i/2)+1):
            if i%j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(find_prime(num1=n1, num2=n2))