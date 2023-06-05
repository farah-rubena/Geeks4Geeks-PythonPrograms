#Python program to add two numbers


#Solution One
number_one = int(input("Enter the first number: "))
number_two = int(input("Eneter the second number: "))

sum_of_numbers = number_one + number_two

print(f"The sum of the two numbers is: {sum_of_numbers}")


#Solution Two
def sum_of_nums(num1, num2):
    
    return num1 + num2

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
summation = sum_of_nums(num1=n1, num2=n2)
print(summation)



#Solution 3 using Lambda 
add_lambda = lambda a,b: a + b
result = add_lambda(3,4)
print(result)