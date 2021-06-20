my_foods=["pizza", "pasta", "cake"]
friend_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)

print("My friend favourite foods are:")
print(friend_foods)

my_foods.append("lasanha")
friend_foods.append("ice cream")

print("My favourite foods are:")
print(my_foods)

print("My friend favourite foods are:")
print(friend_foods)

#Do no use the command friend_food = my_foods as this makes both variables the 
#same, and when we append one, it will append on the other. Use the [:] to copy

for my_food in my_foods:
	print(f"I really love {my_food.title()}")
print("These are my favourite foods.\n")
for friend_food in friend_foods:
	print(f"I really love {friend_food.title()}")
print("These are my friend's favourite foods")