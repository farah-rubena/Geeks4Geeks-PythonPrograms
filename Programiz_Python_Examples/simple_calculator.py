'''WAPP a simple calculator for add, subtract, multiply and divide'''

import os
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1-num2

def multiply(num1,  num2):
    return num1*num2    

def divide(num1, num2):
    return num1/num2

#define a dict with all operations
operation = {
    '+': addition,
    '-': subtraction,
    '*': multiply,
    '/': divide,
}

for _ in operation:
    print(_)

def calculate():

    first_num = float(input("Enter the first number: "))

    multiple_calculation = True
    
    while multiple_calculation: 
        choice = input("Any 1 of the 4 options: ")

        operation_choice = operation[choice]
        second_num = float(input("Enter the second number: "))
        answer = operation_choice(first_num, second_num)
        print(f"The answer for {first_num} {choice} {second_num} = {answer}")

        calculate_again = input("Would, you like o perfoem another calculation ih the same answer?: 'yes' or 'no' OR 'exit' to EXIT the calculator: ").lower()
        if calculate_again == 'yes':
            os.system('cls')
            first_num = answer
        elif calculate_again == 'no':
            calculate()
        elif calculate_again == 'exit':
                multiple_calculation = False
                print("Thankyou for using My Calculator")


calculate()