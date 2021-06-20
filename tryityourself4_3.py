values = []
for value in range(1,21):
	values.append(value)
print(values)

values = []
for value in range(1,1000001):
	values.append(value)

print(min(values))
print(max(values))
print(sum(values))

oddnumbers =[]
for oddnumber in range (1,21,2):
	oddnumbers.append(oddnumber)
print(oddnumbers)

oddnumbers =[]
oddnumbers =[oddnumber for oddnumber in range(1,21,2)]
print(oddnumbers)
threes = [three for three in range(3,31,3)]
print(threes)

cubes =[]
for cube in range(1,11):
	cubes.append(cube**3)
print(cubes)

cubes =[value**3 for value in range (1,11)]
print(cubes)