placestovisit = ["Egypt", "Angola", "Australia", "USA", "Iceland"]
print(placestovisit)
print(sorted(placestovisit))
print("\nThe list is still in the original order:")
print(placestovisit)
print(sorted(placestovisit))
#to reverse temporarly the list use this:
print(sorted(placestovisit,reverse=True))

placestovisit.reverse()
print("here is the reversed list")
print(placestovisit)
placestovisit.reverse()
print("here is the normal list")
print(placestovisit)

print("here is alphabetical order")
placestovisit.sort()
print(placestovisit)
print("here is reversed alphabetical order")
placestovisit.sort(reverse=True)
print(placestovisit)
