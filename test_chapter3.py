#exercice 3-4
dinner_guests = ["tesla", "mozart", "gandhi"]
print(f"You are invited to dinner in my place, dear {dinner_guests[0].title()}")
print(f"You are invited to dinner in my place, dear {dinner_guests[1].title()}")
print(f"You are invited to dinner in my place, dear {dinner_guests[2].title()}")
#exercice 3-5
print(f"Mr. {dinner_guests[0].title()} will no make it to dinner")
dinner_guests[0]="currie"
print(f"You are invited to dinner in my place, dear {dinner_guests[0].title()}")
print(f"You are invited to dinner in my place, dear {dinner_guests[1].title()}")
print(f"You are invited to dinner in my place, dear {dinner_guests[2].title()}")
#exercice 3-6
print(F"Dear guests {dinner_guests[0].title()}, {dinner_guests[1].title()} and {dinner_guests[2].title()}, new seats were found.")
dinner_guests.insert(0, "maria")
dinner_guests.insert(2, "manuel")
dinner_guests.append("antonio")
print(dinner_guests)
#exercice 3-7
print("Unfortunately the new dinner table will not arrive in time, and only two guests will be able to attend")
excluded_dinner=dinner_guests.pop(0)
print(f"Sorry, I can't have you for dinner {excluded_dinner}")
excluded_dinner=dinner_guests.pop(0)
print(f"Sorry, I can't have you for dinner {excluded_dinner}")
excluded_dinner=dinner_guests.pop(0)
print(f"Sorry, I can't have you for dinner {excluded_dinner}")
excluded_dinner=dinner_guests.pop(0)
print(f"Sorry, I can't have you for dinner {excluded_dinner}")
print(f"I will have you for dinner {dinner_guests[0]} and {dinner_guests[1]}.")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)
