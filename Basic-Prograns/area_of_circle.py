'''WAPP to find the area of a circle 
area of circle = pi*r**2'''

#SOLUTION ONE

def area(radius):

    pi = 3.14159
    return pi * (radius**2)

r = float(input("Enter the radius f a circle: "))
print(area(radius=r))
