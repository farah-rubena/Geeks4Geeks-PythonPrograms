'''WAPP to find a number divisibke by another number'''


def divisible_by(divisor, start, end):

    divisible_list = []
    for _ in range(start, end+1):
        if _%divisor == 0:
            divisible_list.append(_)
    return divisible_list

divisor = int(input("Enter the divisor"))
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))
res = divisible_by(divisor, start, end)
print(res)  