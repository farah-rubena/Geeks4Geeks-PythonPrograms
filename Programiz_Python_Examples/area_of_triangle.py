'''WAPP to calculate the area of a Triangle

Area = (base * height) / 2

where "base" represents the length of the base of the triangle, 
and "height" represents the perpendicular distance from the base to the opposite vertex.
'''

#Solution1
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = (base * height)/2

print(f"The area of a Triangle is {area}")
