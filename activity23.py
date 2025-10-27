#listing
x = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']

#functions
x.insert(7, "aug")
print(x)
x.append("sep")
print(x)
x.pop(8)
print(x)
x.remove('aug')
print(x)

#iterations/traversing
for i in x:
    print(i)

#list slicing
name = 'Luis Angelo Z Allarey'
for i in name[0:]:
    print(i)
for i in name[::-1]:
    print(i)
#better slicing 
x.reverse()
print(x)

nam = list(name)
nam.reverse()
print(nam)