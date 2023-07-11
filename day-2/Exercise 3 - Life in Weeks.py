# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

years_remeaning = 90 - age

days = int( 365 * years_remeaning ) 
weeks = int( 52 * years_remeaning )
months = int( 12 * years_remeaning )

print(f"You have {days} days, {weeks} weeks, and {months} months left.")