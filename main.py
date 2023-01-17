# # 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆

# ####################################
# # Write your code below this line 👇

# c = a
# a = b
# b = c

# # Write your code above this line 👆
# ####################################

# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)

# two_digit_number = input("Type a two digit number: ")
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# result = int(height) / (int(weight) ** 2)
# print("Your BMI is " + str("%.2f" % result))

# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# target_age = 90
# time_to_target = target_age - int(age)
# month = time_to_target * 12
# weeks = time_to_target * 52
# days = time_to_target * 365
# print("You have " + str(days) + " days, " +
#       str(weeks) + " weeks, and " + str(month) + " months, " + "left.")
# message = f"You have {days}, {weeks}, and {month} left"
# print(message)

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# amount = input("Amount? ")
# number_guests = input("Participents? ")
# tip = input("How many tip? ")
# each_to_pay = (int(amount) / int(number_guests))
# result = (each_to_pay / 100) * (int(tip) + 100)
# message = f"Each one pays {round(result, 2)} $"
# print(message)

# # Choose number to evaluate 💯
# number = int(input("Which number do you want to check? "))
# # code goes below this line

# if (number % 2) == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# result = round((weight / height**2))
# if result >= 35:
#     print(f"Your BMI is {result} you are clinically obese")
# elif result >= 30:
#     print(f"Your BMI is {result} you are  obese")
# elif result >= 25:
#     print(f"Your BMI is {result} you are slightly overweight")
# elif result >= 18.5:
#     print(f"Your BMI is {result} you have a normal weight")
# else:
#     print(f"Your BMI is {result} you are underweight")
