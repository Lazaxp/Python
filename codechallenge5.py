print("Good Day \tWhat manga would you like?")
genr = str(input("What genre are you looking for? (Romance, Comedy, Horror, Action, Mystery)\t").lower())
length = str(input("How long is the manga you're looking for?(Long, Short, Medium)\t").lower())
dat = eval(input("What year of publication are you interested in?(1990, 2000, 2010)\t"))

if genr == "romance":
	print(genr)
	if length == "long":
		print(length)
		if dat == 1990:
			print(dat)
			Print("Long Romance Mangas in the 1990's:\nNone Found")
		elif dat == 2000:
			print(dat)
			print("Long Romance Mangas in the 2000's:\nNone Found")
		elif dat == 2010:
			print(dat)
			pirnt("Long Romance Mangas in the 2010's:\nRent-A-Girlfriend\n")
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
			print("Short Romance Mangas in the 1990's:\n")
		elif dat == 2000:
			print(dat)
			print("Short Romance Mangas in the 2000's:\nClannad\nSoranin")
		elif dat == 2010:
			print(dat)
			print("Short Romance Mangas in the 2010's:\nNisekoi\nThe World God Only Knows\nThe Dangers of my Heart\nMy Dress Up Darling\nRascal Does Not Dream of a Bunny Girl")
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
			print("Medium Romance Mangas in the 1990s")
		elif dat == 2000:
			print(dat)
			print("Medium Romance Mangas in the 1990s")
		elif dat == 2010:
			print(dat)
			print("Medium Romance Mangas in the 1990s")
		else:
			print("Please choose within the Options")
	else:
		print("Please choose within the Options.")
elif genr == "comedy":
	print(genr)
	if length == "long":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	else:
		print("Please choose within the Options.")
elif genr == "horror":
	print(genr)
	if length == "long":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	else:
		print("Please choose within the Options.")
elif genr == "action":
	print(genr)
	if length == "long":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	else:
		print("Please choose within the Options.")
elif genr == "Mystery":
	print(genr)
	if length == "long":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
		elif dat == 2000:
			print(dat)
		elif dat == 2010:
			print(dat)
		else:
			print("Please choose within the Options")
	else:
		print("Please choose within the Options.")
else:
	print("Please choose within the Options.")