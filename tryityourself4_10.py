placestovisit = ["Egypt", "Angola", "Australia", "USA", "Iceland"]
print("The first three items of the list are:")
print(placestovisit[:3])
print("The  three items from the middle of the list are:")
print(placestovisit[1:4])
print("The last three items of the list are:")
print(placestovisit[-3:])

pizzas = ["peperonni","napolitana","capricciosa"]
friend_pizzas = pizzas[:]
pizzas.append("margerita")
friend_pizzas.append("cheese")
print("My favourite pizzas are:")
print(pizzas)
print("My friend favourite pizzas are:")
print(friend_pizzas)
