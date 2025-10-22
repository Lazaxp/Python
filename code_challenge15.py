anilist = []
while True:
  show = input("Reccomend any anime for me").capitalize()
  anilist.append(show)
  if show == "Rent-a-girlfriend" or show == "Rent a girlfriend":
    print("pass")
    anilist.remove(show)
  elif show == "Initial d":
    print("K-kansei dorifuto??")
  elif show == "Saiki k" or show == "The disastrous life of saiki k":
    print("GOAT.")
  else:
    print("cool!")
  if show == "Exit":
    print("Reccomendation ended")
    break
print("Here were your selection")
for x in anilist
  print(f",{x}")
print("Thank you!")  
    
