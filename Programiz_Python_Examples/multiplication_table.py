'''WAPP to display multiplication table'''

def table(num):

    for _ in range(1, num+1):
        result = num*_
        print(f"{num}*{_} = {result}")

n = int(input("Enter a number:"))
table(num=n)
