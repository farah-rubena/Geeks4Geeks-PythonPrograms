'''Programs to print triangles using *, numbers and characters'''

def triangles(rows):

    for j in range(rows):
        for i in range(j+1):
            print('* ', end="")
        print("\n")

r = int(input("Enter the number of rows: "))
triangles(rows=r)