#creating a options with while loop and functions
def activity1():
    print ("Hello World")
    print ("ANG PAGBABALIK NI YORME")
    x = 5
    print("The Value of X is:", x)

def activity2():
    name = input("Hi, what is your name")
    print("Hello", name,"Welcome to the Matrix")

def activity3():
    print("Good Morning \n\tAfternoon \n\t\tnight")
    print("Sir Mesiera")

def activity4():
    name = input("what is your name ->")
    print("your name has",len(name) ,"characters")

def activity5():
    calc = eval(input("when were you born? >>"))
    print("The data type of this file is",type(calc))
    answer = 2025 - calc
    print("Youre",answer,"years old")

def activity6():
    n1 = eval(input("enter first number:"))
    n2 = eval(input("enter second number:"))
    s = n1 + n2
    d= n1 - n2
    p = n1 * n2
    q = n1 / n2
    print("the sum of",n1,"and",n2, "is equal to",s)
    print("the difference of",n1,"and",n1,"is equal to",d)
    print("the product of",n1,"and",n2,"isequal to",p)
    print("the quotient of",n1,"and",n2,"is equal to",q)

def activity7():
    a = 10
    print("The value of a is:", a)

    a += 10
    print("The value of a is:", a)

    a /= 10
    print("The amount of 5s in a is",a)

def activity8():
    a = 30
    b = 31

    print(a < b)
    print("a is less than b")

def activity9():
    year = '2025'
    month = 'august'

    print((year == '2025') and (month == 'august'))
    print("it is currently the month of August in the year 2025")

def activity11():
    temp = eval(input("What is the temperature?\t"))
    if temp <= (-1):
	    print("Temp is; Freezing Cold")
    elif temp >= 1 and temp <=20:
	    print("Temp is; U cold buddy")
    elif temp >= 21 and temp <=30:
	    print("Temp is; Lukewarm")
    elif temp >= 31 and temp <=40:
	    print("Temp is; Warm")
    elif temp >= 41 and temp <= 50:
	    print("Temp is; hot! hot!")
    elif temp >= 51:
	    print("Temp is; Boiling Hot")
    else:
	    print("?")
          
def activity10():
    name = input("What is your name?:")
    print("regular fare is 13")
    question = input("Are you a regular passenger?:")

    if question =="yes":
	    print("Your Fare is the Regular Fare")

    else:
	    fare = 13
	    discount = fare *.2
	    newfare = fare - discount
	    print("congrats",name,"your new fare is",newfare)
def activity12():
      #For loops
    for x in range (11):
        print(x,"- Hello World")

def activity13():
    #use for loops to ask user 10 numbers and add the sum
    num = 0
    for x in range (10):
        sum = eval(input("Input 10 numbers\t>>"))
        num += sum
        print("Current Total:",num)
    print("The Total is",num)
def activity14():
      #output in descending order
    for x in range (20, 0, -1):
        print(x)
def activity15():
    #output even numbers only
    for x in range (2, 21, 2):
        print(x)    
def activity16():
    #using for loops to print horizontally
    for x in range(1,11):
       print(x,end=(","))
def activity17():
    for x in range(1,11):
        for y in range(1,11):
            print(y,end=" ")
        print()
def activity18():
    for x in range (1,11):
        for y in range(1,x):
            print(x,end=" ")
        print()
def activity19():
    for x in range (1,11):
        for y in range(1,x):
            print("*",end=" ")
        print()
def activity20():
    for x in range (1,11):
    # for y in range(1,x):
    #     print("*",end=" ")
    # print()
        for z in range(1,x):
            print("*",end=" ")
        print()
def activity21():
     #application of the while loopx = True
    x = True
    while x == True:
        kid = input('Are we there yet?\t')
        if kid == 'no':
            print('aww')
            continue
        elif kid== 'yes':
            print('Yay!')
            break
        else:
            (':(')
def activity22():
    import random

    x = random.randint(1,10)
    while True:
        g = eval(input("Guess the Number!!(1,10):\t"))
        if g == x:
            print(f"Number: {x} You Win!!")
            break
        else:
            print("Try again!!")
def activity23():
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
def activity24():
    #defined functions
    def greet(name):
        print(f"hi, {name} how you doing?")

    def sum(a):
        x = 0 
        for y in range(a, 0,-1):
            x += y
        print(f"the sum of {a} is {x}")

    greet("Luis")
    sum(5)
def activity25():
     print("this is technically a wider version of activity 25")
def activity26():
    pr_lang = {"Python", "PHP", "MySQL", "JavaScript", "CSS", "C++"}
    pr_langu = {"Python" : "Madali", "PHP" : "Pera", "JavaScript" : "Mahirap", "CSS" : "Mas Mahirap", "C++" : "Pang Minecraft"}

    print(pr_lang[4])
