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
#printing the reverse order of the list, is permanent. We can always rollback the changes if we use the reverse() command again.
cars.reverse()
print(cars)
cars.reverse()
print(cars)

#to find the lenght of a list, use the len() command
len(cars)
