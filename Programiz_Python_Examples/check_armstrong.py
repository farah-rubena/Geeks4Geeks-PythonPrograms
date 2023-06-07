'''WAPP to check Armstrong Number'''

def amstrong_check(num):

    number_len = len(num)
    res = 0
    
    for _ in num:
        _ = int(_)
        res +=  _**number_len
    
    if res == int(num):
        return "Is Armstrong"
    else:
        return "Not Armstrong"


n = input("Enter the number: ")
result = amstrong_check(num=n)
print(result)