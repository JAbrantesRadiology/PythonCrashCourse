answer = 17
if answer != 42:
	print("That is not the correct answer.")


age= 19
print(age<21)
print(age>15)
print(age<=21)
print(age>22)

#To check if two conditions are both true at the same time, use the "and" - if
#both conditions are passed, the True value is given.

print("\nNew test 'And' ")
age_0 = 22
age_1 = 18
print(age_0 >=21 and age_1 >=21)
age_0 = 22
age_1 = 21
print(age_0 >=21 and age_1 >=21)

#For readability
print((age_0>=21) and (age_1 >=21))

#To check if any of the conditions are true , use the "or" - if
#one of the conditions passes, the True value is given.
print("\nNew test 'Or' ")
age_0 = 22
age_1 = 18
print(age_0 >=21 or age_1 >=21)
age_0=18
print(age_0 >=21 or age_1 >=21)