# Define a float
# y = 1.
# print(y)
# print(type(y))
# Convert float to integer with the int function
# z = int(y)
# print(z)
# print(type(z))
# print(3 * True)
# print(-3.1 * True)
# print(type("abc" * False))
# print(len("abc" * False))
# PEMDAS
# () 
# **
# */
# +-
# print(3/3+3*3-3)
# weight_as_int=int(8)
# height_as_float=float(1.72)
# Using the exponent operator **
# bmi=weight_as_int/height_as_float ** 2
# or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)
# bmi_as_int = int(bmi)
# print(bmi_as_int)
# score = 0
# height = 1.8
# isWinning = True
# f-String
# print(f"your score is {score}, your height is {height},you are winning is {isWinning}")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# Months_remaining = years_remaining * 12
# Message = f"You have{days_remaining} days, {weeks_remaining} weeks,"
# print(Message)
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150/5) * 1.12
# Round the result to 2 decimals places = 33.60
print("Welcome to the calculator!")
Bill = float(input("What is the total bill? $"))
Tip = int(input("How much tip would you like to do? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person)
print(f"Each person should pay ${final_amount}")
#bill_with_tip = Tip / 100 * Bill + Bill
#another one bill_with_tip = bill * (1 + tip/ 100)

