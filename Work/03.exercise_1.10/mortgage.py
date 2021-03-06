# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_of_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if  extra_payment_start_month <= number_of_months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    number_of_months += 1
    if principal < 0:
        principal = 0
    print(number_of_months, round(total_paid, 2), round(principal, 2))

print(f'Total paid: {total_paid:0.1f}')
print(f'Months: {number_of_months}')
