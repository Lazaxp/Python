name = input("What is your name?:")
print("regular fare is 13")
question = input("Are you a regular passenger?:")

if question =="yes":
	print("Your Fare is the Regular Fare")

else:
	fare = 13
	discount = fare *.2
	newfare = fare - discount
	print("congrates",name,"your new fare is",newfare)
