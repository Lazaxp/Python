#print a pyramid of palimdrome numbers
for a in range (1, 11):
  for x in range(10,a,-1):
    print(" ",end=" ")
  for y in range (1,a):
    print(a-y,end=" ")
  for z in range (1,a-1):
    print(1+x,end=" ")
  print()
