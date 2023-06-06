'''WAPP to swap varaibles'''

#Soltion 1

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
#swap 
temp = a
a = b 
b = temp
print(f"The new value of 'a' is {a} and new value of 'b' is {b}")

def swap_var(a,b):

    c = a
    a = b
    b = c

    return a, b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(swap_var(a,b))