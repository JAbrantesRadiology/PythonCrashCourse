squares =[]
for value in range (1,11):
	square = value ** 2
	squares.append(square)
print(squares)

#It is not needed the part square=Value, we can omit this temporary value

squares =[]
for value in range (1,11):
	squares.append(value**2)
print(squares)

#we can use the list comprehension to make a list in one line of code. No : is needed for this for loop in a single line
squares1 = [value**2 for value in range(1,11)]
print(squares1)