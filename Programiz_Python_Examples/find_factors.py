'''WAPP to fidn the factors of a number: 
Factors of a number are the numbers that divide the given number without leaving a remainder.
 For example, the factors of 12 are 1, 2, 3, 4, 6, and 12.'''


def finding_factors(num):

    factors_list = []
    for _ in range(1, num+1):
        if num%_ == 0:
            factors_list.append(_)

    return factors_list

n = int(input("Enter a number: "))
res = finding_factors(num=n)
print(f"The factors of {n} are {res}")