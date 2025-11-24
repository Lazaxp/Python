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

def activity10():
    name = input("What is you name?:")
    student = input("Hi", name,"are you a regular passenger?"
