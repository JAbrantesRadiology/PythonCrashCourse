#This is a tuple, it cant be changed after created. Use inside () insted of []
dimensions=(200,50)
print("Original dimensions")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print("\n New dimensions:")
for dimension in dimensions:
	print(dimension)