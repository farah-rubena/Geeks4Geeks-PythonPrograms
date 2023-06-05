'''Wap to find Armstorng number
Number that is equal to the sum of its own digits each raised to the power of the number of the digits in that number
153 '''


def find_armstring(num):
    num_len = len(num)
    armstrong_num = 0

    for n in num:
        n = int(n)
        armstrong_num += n**num_len

    if armstrong_num == int(num):
        return "Is Armstrong"
    else:
        return "Not Armstrong"

n = input("Enter the number to be checked: ")
print(find_armstring(num=n))