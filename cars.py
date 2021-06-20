cars = ['bmw', 'audi', "toyota", "subaru"]
#sort by alphabetical order, but permanently
cars.sort()
print(cars)
#Carefull - True must be capitallized
cars.sort(reverse=True)
print(cars)

#if we dont want a permanent change, we can use the command sorted
cars = ['bmw', 'audi', "toyota", "subaru"]
print("The original list is:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nThe original list again is:")
print(cars)
#printing the reverse order of the list, is permanent. We can always rollback 
#the changes if we use the reverse() command again.
cars.reverse()
print(cars)
cars.reverse()
print(cars)

#to find the lenght of a list, use the len() command
len(cars)

#Chapter 5 Work - If and conditional tests

for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

car ="audi"
print("\nEx 1:")
print(car=="bmw")

#The problem of capitalization
car ="Audi"
print("\nEx 2:")
print(car=="audi")

#Fix the capitalization problem
car ="Audi"
print("\nEx 3:")
print(car.lower()=="audi")
print(car)
