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
			pirnt("Long Romance Mangas in the 2010's:\nKomi Can't Communicate")
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
			print("Short Romance Mangas in the 1990's:\nKaguya Hime")
		elif dat == 2000:
			print(dat)
			print("Short Romance Mangas in the 2000's:\nClannad\nSoranin")
		elif dat == 2010:
			print(dat)
			print("Short Romance Mangas in the 2010's:\nThe Dangers of my Heart\nMy Dress Up Darling\nRascal Does Not Dream of a Bunny Girl")
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
			print("Medium Romance Mangas in the 1990's:\nNANA")
		elif dat == 2000:
			print(dat)
			print("Medium Romance Mangas in the 2000's:\nNisekoi\nThe World God Only Knows")
		elif dat == 2010:
			print(dat)
			print("Medium Romance Mangas in the 2010's:\nKaguya-Sama:Love is War")
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
			print("Long Comedy Mangas in the 1990's:\nCrayon Shin-chan")
		elif dat == 2000:
			print(dat)
			print("Long Comedy Mangas in the 2000's:\nGintama")
		elif dat == 2010:
			print(dat)
			print("Long Comedy Mangas in the 2010's:Gekkan Shoujo Nozaki-kun")
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
			print("Short Comedy Mangas in the 1990's:\nGolden Boy")
		elif dat == 2000:
			print(dat)
			print("Short Comedy Mangas in the 2000's:\nYotsuba-to!")
		elif dat == 2010:
			print(dat)
			print("Short Comedy Mangas in the 2010's:\nThe Disastrous Life of Saiki K.")
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
			print("Medium Comedy Mangas in the 1990's:\nRanma 1/2")
		elif dat == 2000:
			print(dat)
			print("Medium Comedy Mangas in the 2000's:\nSeitokai no Yakuindomo")
		elif dat == 2010:
			print(dat)
			print("Medium Comedy Mangas in the 2010's:\n")
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
			print("Long Horror Mangas in the 1990's:\nNone Found")
		elif dat == 2000:
			print(dat)
			print("Long Horror Mangas in the 2000's:\nNone Found")
		elif dat == 2010:
			print(dat)
			print("Long Horror Mangas in the 2010's:\nNone Found")
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
			print("Short Horror Mangas in the 1990s:/nUzumaki\nMirai Nikki")
		elif dat == 2000:
			print(dat)
			print("Short Horror Mangas in the 2000's:\nAnother")
		elif dat == 2010:
			print(dat)
			print("Short Horror Mangas in the 2010's:\nMieruko-chan")
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
			print("Medium Horror Mangas in the 1990s:\nJunji Ito Horror Collection Book")
		elif dat == 2000:
			print(dat)
			print("Medium Horror Mangas in the 2000's:\nNone Found")
		elif dat == 2010:
			print(dat)
			print("Medium Horror Mangas in the 2010's:\nNone Found")
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
			print("Long Action Mangas in the 1990's\n:One Piece")
		elif dat == 2000:
			print(dat)
			print("Long Action Mangas in the 2000's:\nBleach")
		elif dat == 2010:
			print(dat)
			print("Long Action Mangas in the 2010's:\nBlack Clover")
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
			print("Short Action Mangas in the 1990's:\nAlita Battle Angel")
		elif dat == 2000:
			print(dat)
			print("Short Action Mangas in the 2000's:\nCard Captor Sakura")
		elif dat == 2010:
			print(dat)
			print("Short Action Mangas in the 2010's:\nMob Psycho 100")
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
			print("Medium Action Mangas in the 1990s:\nInitial D")
		elif dat == 2000:
			print(dat)
			print("Medium Action Mangas in the 2000's:\nKuroko no Basketball")
		elif dat == 2010:
			print(dat)
			print("Medium Action Mangas in the 2010's:\nFire Force")
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
			print("Long Mystery Mangas in the 1990s:\nDetective Conan")
		elif dat == 2000:
			print(dat)
			print("Long Mystery Mangas in the 2000's:None Found")
		elif dat == 2010:
			print(dat)
			print("Long Mystery Mangas in the 2010's:None Found")
		else:
			print("Please choose within the Options")
	elif length == "short":
		print(length)
		if dat == 1990:
			print(dat)
			print("Short Mystery Mangas in the 1990's:None Found")
		elif dat == 2000:
			print(dat)
			print("Short Mystery Mangas in the 2000's:\nUmineko: When They Cry")
		elif dat == 2010:
			print(dat)
			print("Short Mystery Mangas in the 2010's:\nAnohana: The Flower we saw that Day")
		else:
			print("Please choose within the Options")
	elif length == "Medium":
		print(length)
		if dat == 1990:
			print(dat)
			print("Medium Mystery Mangas in the 1990's:\nThe Case Files of Young Kindaichi")
		elif dat == 2000:
			print(dat)
			print("Medium Mystery Mangas in the 2000's:\nStein's Gate")
		elif dat == 2010:
			print(dat)
			print("Medium Mystery Mangas in the 2010's:\nSummertime Rendering")
		else:
			print("Please choose within the Options")
	else:
		print("Please choose within the Options.")
else:

	print("Please choose within the Options.")

