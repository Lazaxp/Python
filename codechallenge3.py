
un1='Laza'
ps2='Dugitoka'


ign = input("what is your username?>>")

if ign==un1:
	pp=input("Enter your password>>")
	if pp==ps2:
		print("welcome")
	else:
		print("Incorrect password")
		
else:
	print("Username not found.")