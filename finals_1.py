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
    for x in range (1,11):
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
        x += 1
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

def activity24_1():
    from activity24 import sum, greet
    greet("Allarey")
    sum(5)

def activity25():
    print("this is technically a wider version of activity 25")
    print("so i wont show it because its still this program")


def activity26():
    pr_lang = {"Python", "PHP", "MySQL", "JavaScript", "CSS", "C++"}
    pr_langu = {"Python" : "Madali", "PHP" : "Pera", "JavaScript" : "Mahirap", "CSS" : "Mas Mahirap", "C++" : "Pang Minecraft"}

    print(pr_lang[4])

def activity27():
     #adding dictionary
    empty_dictionary = {}
    def print_anime():
        for x,y in empty_dictionary.items():
            print(f"CODE -- {x} ANIME -- {y}")
    def search(key):
        print(f"Result shows {empty_dictionary[key]} on the List")

        print("Save your anime List")
    while True:
        keys = input("Keys for this anime(EX. OP for One Piece):\t")
        value = input("Anime Title:\t")
        empty_dictionary[keys] = value

        x = input("Continue?(yes/no/print/search):\t").lower()

        if x == "yes":
            continue
        elif x == "no":
            print("Program Cancelled")
            break
        elif x == "print":
            print_anime()
        elif x == "search":
            key = input("Type the code of the anime:")
            search(key)
        else:
            print("Select within the choices")


def activity28():
    #Step 1 
    import pygame, time, random

    # Initialize Pygame
    pygame.init()

    # Screen size
    width = 600
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Colors (RGB)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)

    # Game speed and block size
    clock = pygame.time.Clock()
    speed = 10
    snake_block = 10

    # Font for messages
    font_style = pygame.font.SysFont(None, 30)


    #Step 2 
    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    #Step 3 
    def game_loop():
        game_over = False
        game_close = False

        # Starting position of the snake
        x = width / 2
        y = height / 2

        x_change = 0
        y_change = 0

        snake_list = []
        length_of_snake = 1

        # Generate first food
        food_x = round(random.randrange(0, width - snake_block) / 10) * 10
        food_y = round(random.randrange(0, height - snake_block) / 10) * 10

        while not game_over:

            # Loss screen
            while game_close:
                screen.fill(black)
                message = font_style.render('You Lost! Press Q-Quit or C-Play Again', True, red)
                screen.blit(message, [width / 6, height / 3])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()

            # Event handling (keyboard)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0

            # Check if snake hits the wall
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            # Update position
            x += x_change
            y += y_change

            # Draw background and food
            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            # Add snake head
            snake_head = [x, y]
            snake_list.append(snake_head)

            # Remove extra segments if not growing
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Check self-collision
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            # Draw the snake
            draw_snake(snake_list)

            # Update display
            pygame.display.update()

            # Check if snake eats food
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10) * 10
                food_y = round(random.randrange(0, height - snake_block) / 10) * 10
                length_of_snake += 1

            # Control game speed
            clock.tick(speed)

        # Quit Pygame
        pygame.quit()
        quit()

    # Start the game
    game_loop()
def    cchallenge2():
    deposit = eval(input("enter your deposit>>"))
    print("type:",type(deposit))
    t = deposit//1000
    f = (deposit % 1000)//500
    tw = (deposit % 1000 % 500)//200
    on = (deposit % 1000 % 500 % 200)//100
    fi = (deposit % 1000 % 500 % 200 % 100)//50
    twe = (deposit % 1000 % 500 % 200 % 100 % 50)//20
    ten = (deposit % 1000 % 500 % 200 % 100 % 50 % 20)//10
    fiv = (deposit % 1000 % 500 % 200 % 100 % 50 % 20 % 10)//5
    one = (deposit % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5)//1
    print("1000 =",t,"\n500 =",f,"\n200 =",tw,"\n100 =",on,"\n50 =",fi,"\n20 =",twe,"\n10 =",ten,"\n5 =",fiv,"\n1 =",one)
def    cchallenge5():
    print("Good Day \tWhat manga would you like?")
    genr = str(input("What genre are you looking for? (Romance, Comedy, Horror, Action, Mystery)\t").lower())
    length = str(input("How long is the manga you're looking for?(Long, Short, Medium)\t").lower())
    dat = eval(input("What year of publication are you interested in?(1990, 2000, 2010)\t"))

    if genr == "romance":
        print(genr)
        if length == "long" and dat == 1990:
            print(dat)
            Print("Long Romance Mangas in the 1990's:\nNone Found")
        elif length == "long" and dat == 2000:
            print(dat)
            print("Long Romance Mangas in the 2000's:\nNone Found")
        elif length == "long" and dat == 2010:
            print(dat)
            pirnt("Long Romance Mangas in the 2010's:\nKomi Can't Communicate")
        elif length == "short" and dat == 1990:
            print(dat)
            print("Short Romance Mangas in the 1990's:\nKaguya Hime")
        elif length == "short" and dat == 2000:
            print(dat)
            print("Short Romance Mangas in the 2000's:\nClannad\nSoranin")
        elif length == "short" and dat == 2010:
            print(dat)
            print("Short Romance Mangas in the 2010's:\nThe Dangers of my Heart\nMy Dress Up Darling\nRascal Does Not Dream of a Bunny Girl")
        elif length == "Medium" and dat == 1990:
            print(dat)
            print("Medium Romance Mangas in the 1990's:\nNANA")
        elif length == "Medium" and dat == 2000:
            print(dat)
            print("Medium Romance Mangas in the 2000's:\nNisekoi\nThe World God Only Knows")
        elif length == "Medium" and dat == 2010:
            print(dat)
            print("Medium Romance Mangas in the 2010's:\nKaguya-Sama:Love is War")
        else:
            print("Please choose within the Options.")
    elif genr == "comedy":
        print(genr)
        if length == "long" and dat == 1990:
            print(dat)
            print("Long Comedy Mangas in the 1990's:\nCrayon Shin-chan")
        elif length == "long" and dat == 2000:
            print(dat)
            print("Long Comedy Mangas in the 2000's:\nGintama")
        elif length == "long" and dat == 2010:
            print(dat)
            print("Long Comedy Mangas in the 2010's:Gekkan Shoujo Nozaki-kun")
        elif length == "short" and dat == 1990:		
            print(dat)
            print("Short Comedy Mangas in the 1990's:\nGolden Boy")
        elif length == "short" and dat == 2000:
            print(dat)
            print("Short Comedy Mangas in the 2000's:\nYotsuba-to!")	
        elif length == "short" and dat == 2010:
            print(dat)
            print("Short Comedy Mangas in the 2010's:\nThe Disastrous Life of Saiki K.")
        elif length == "Medium" and dat == 1990:
            print(dat)
            print("Medium Comedy Mangas in the 1990's:\nRanma 1/2")
        elif length == "Medium" and dat == 2000:	
            print(dat)
            print("Medium Comedy Mangas in the 2000's:\nSeitokai no Yakuindomo")
        elif length == "Medium" and dat == 2010:
            print(dat)
            print("Medium Comedy Mangas in the 2010's:\n")
        else:
            print("Please choose within the Options.")
    elif genr == "horror":
        print(genr)
        if length == "long" and dat == 1990:
            print(dat)
            print("Long Horror Mangas in the 1990's:\nNone Found")
        elif length == "long" and dat == 2000:
            print(dat)
            print("Long Horror Mangas in the 2000's:\nNone Found")
        elif length == "long" and dat == 2010:
            print(dat)
            print("Long Horror Mangas in the 2010's:\nNone Found")
        elif length == "short" and dat == 1990:
            print(dat)
            print("Short Horror Mangas in the 1990s:/nUzumaki\nMirai Nikki")
        elif length == "short" and dat == 2000:
            print(dat)
            print("Short Horror Mangas in the 2000's:\nAnother")
        elif length == "short" and dat == 2010:
            print(dat)
            print("Short Horror Mangas in the 2010's:\nMieruko-chan")
        elif length == "Medium" and dat == 1990:
            print(dat)
            print("Medium Horror Mangas in the 1990s:\nJunji Ito Horror Collection Book")
        elif length == "Medium" and dat == 2000:
            print(dat)
            print("Medium Horror Mangas in the 2000's:\nNone Found")
        elif length == "Medium" and dat == 2010:
            print(dat)
            print("Medium Horror Mangas in the 2010's:\nNone Found")
        else:
            print("Please choose within the Options.")
    elif genr == "action":
        print(genr)
        if length == "long" and dat == 1990:
            print(dat)
            print("Long Action Mangas in the 1990's\n:One Piece")
        elif length == "long" and dat == 2000:
            print(dat)
            print("Long Action Mangas in the 2000's:\nBleach")
        elif length == "long" and dat == 2010:
            print(dat)
            print("Long Action Mangas in the 2010's:\nBlack Clover")
        elif length == "short" and dat == 1990:
            print(dat)
            print("Short Action Mangas in the 1990's:\nAlita Battle Angel")
        elif length == "short" and dat == 2000:
            print(dat)
            print("Short Action Mangas in the 2000's:\nCard Captor Sakura")
        elif length == "short" and dat == 2010:
            print(dat)
            print("Short Action Mangas in the 2010's:\nMob Psycho 100")
        elif length == "Medium" and dat == 1990:
            print(dat)
            print("Medium Action Mangas in the 1990s:\nInitial D")
        elif length == "Medium" and dat == 2000:
            print(dat)
            print("Medium Action Mangas in the 2000's:\nKuroko no Basketball")
        elif length == "Medium" and dat == 2010:
            print(dat)
            print("Medium Action Mangas in the 2010's:\nFire Force")
        else:
            print("Please choose within the Options.")
    elif genr == "Mystery":
        print(genr)
        if length == "long" and dat == 1990:
            print(dat)
            print("Long Mystery Mangas in the 1990s:\nDetective Conan")
        elif length == "long" and dat == 2000:
            print(dat)
            print("Long Mystery Mangas in the 2000's:None Found")
        elif length == "long" and dat == 2010:
            print(dat)
            print("Long Mystery Mangas in the 2010's:None Found")
        elif length == "short" and dat == 1990:
            print(dat)
            print("Short Mystery Mangas in the 1990's:None Found")
        elif length == "short" and dat == 2000:
            print(dat)
            print("Short Mystery Mangas in the 2000's:\nUmineko: When They Cry")
        elif length == "short" and dat == 2010:
            print(dat)
            print("Short Mystery Mangas in the 2010's:\nAnohana: The Flower we saw that Day")
        elif length == "Medium" and dat == 1990:
            print(dat)
            print("Medium Mystery Mangas in the 1990's:\nThe Case Files of Young Kindaichi")
        elif length == "Medium" and dat == 2000:
            print(dat)
            print("Medium Mystery Mangas in the 2000's:\nStein's Gate")
        elif length == "Medium" and dat == 2010:
            print(dat)
            print("Medium Mystery Mangas in the 2010's:\nSummertime Rendering")
        else:
            print("Please choose within the Options.")
    else:

        print("Please choose within the Options.")
def    cchallenge8():
    #Display a multiplication table based upon user Input.
    print("Multiplication Table Display\n")
    numero = eval(input("Input a Number from 1-9:\t"))
    for x in range (1,11):
        disp = numero * x
        print(numero,"x",x,"=",disp)
def    cchallenge15():
    anilist = []
    while True:
        show = input("Reccomend any anime for me(kindly type exit to stop):\t").capitalize()
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
        for x in anilist:
            print(f"- {x}")
            print("Thank you!")  
def    cchallenge16():
    import os, json
    records = {}
    with open('record.json', 'r') as new_file:
        record = json.load(new_file)
    records = record
    while True:
        print("Welcome to Student Record Program - Select from the Options Below:\n\n")
        print("Add - Add Info\nSrh - Search Info\nDel - Delete a Record\nMod - Modify Recored\nAll - Show all current Records\nExp - Export Data")
        res = input("Type here:\t").capitalize()
        os.system("cls")
        if res == "Add":
            
            print("- Add a your Students Info -\n")
            code = input("Input Student Key:\t")
            fname = input("Input Student First Name:\t").upper()
            lname = input("Input Student Last Name:\t").upper()
            course = input("Input Student Course:\t").upper()
            email = input("Input Student Email Address:\t").upper()
            os.system("cls")
            records[code] = []
            records = {code :[fname, lname, course, email]}
            print("Data has been Recorded.\n\n")
        elif res == "Search":
            print("- Search Student Records - ")
            key = input("Input here your Student Key:\t").upper()
            os.system("cls")
            for x in records.keys():
                if key in records.keys():
                    print("Record Found")
                    for y in records[key]:
                        print(f" - {y}")
                else:
                    print("Record Not Found")
                break
        elif res == "Del" or res == "Delete":
            os.system("cls")
            print("- Delete Student Record -")
            key = input("\n\nEnter Student Key to Delete:\t")
            records.pop(key)
            os.system("cls")
            print(f"\nRecord deleted.\n")
        elif res == "Mod":
            os.system("cls")
            print("- Modify a Students Record -")
            key = input("Input Student Key to Modify:\t\t")
            if key in records.keys():
                print("Record Found")
                for y in records[key]:
                    print(f" - {y}")
                print("Input Student Record to modify:\nf - Student First Name\nl - Student Last Name\nC - Student Course\n@ - Student Email")
                sel = input("Type Here:\t").capitalize()
                if sel == "F":
                    fname = input("Input Student First Name:\t").upper()
                    records[key][0] = fname
                elif sel == "L":
                    lname = input("Input Student Last Name:\t").upper()
                    records[key][1] = lname
                elif sel == "C":
                    course = input("Input Student Course:\t").upper()
                    records[key][2] = course
                elif sel == "@":
                    email = input("Input Student Email Address:\t").upper()
                    records[key][3] = email
                    if "@.com" in email:
                        continue
                    else:
                        print("Invalid Email")
                else:
                    print("Please select from the options.")
                os.system("cls")
                records = {code :[fname, lname, course, email]}
                print("Data Modified")
            else:
                print("Record Not Found")
        elif res == "All":
            os.system("cls")
            print("- All Student Records -")
            for x, y in records.items():
                print(f"Student ID: {x} Record: {y}")
                break
        elif res == "Exp":
            os.system("cls")
            print("- Export Record -\n\n")
            with open('record.json', 'w') as new_file:
                record = json.dump(records,new_file,indent=4)
            records = record
            print("Data Exported to record.json\n\n")
        else:
            os.system("cls")
            print("\nPlease Select within the Options.\n")

