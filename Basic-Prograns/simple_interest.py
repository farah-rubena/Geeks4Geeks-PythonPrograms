'''WAPP for imple interest
(P*R*T/100) straightforward formula based on three key components: the principal amount (the initial sum of money), 
the interest rate (the percentage charged on the principal), and the time period (the duration for which the interest is calculated).
'''

#SOLUTUON ONE
principal_amount = float(input("Enter the initial amount: "))
rate_of_interest = float(input("ENter the rate of interest: "))
time_period = float(input("Enter the time period: "))

calculate_simpleinterest = (principal_amount * rate_of_interest * time_period) / 100
print(calculate_simpleinterest)

#SOLUTON TWO
def simple_interest(p, r, t):

    return (p*r*t)/100

principal_amount = float(input("Enter the initial amount: "))
rate_of_interest = float(input("ENter the rate of interest: "))
time_period = float(input("Enter the time period: "))
print(simple_interest(p=principal_amount, r=rate_of_interest, t=time_period))