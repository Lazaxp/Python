#Print a triangle shaped set of asterisks
print("\t\t *t",end="")
for x in range (1, 11):
  for y in range (10,x,-1):
    print(" ",end="")
  for z in range (1,x,1):
    print("*",end="")
  for i in range (1,x,1):
    print("*",end="")
  print()

