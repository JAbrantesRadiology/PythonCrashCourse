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