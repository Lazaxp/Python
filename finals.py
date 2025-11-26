from finals_1 import *
name = input("Hi, Whats your Name?:\t").capitalize()
while True:
    print(f"\n\nWelcome {name} to my Code Compiler.\nSelect a program section you want to run:")
    sel = input("A - Activity 1-5\nB - Activity 6-10\nC - Activity 11-15\nD - Activity 16-20\nE - Activity 21-24\nType Here:\t").upper()
    if sel == "A":
        al = input("\n\nSelected Section A:\nA - Activity 1\nB - Activity 2\nC - Activity 3\nD - Activity 4\nE - Activity 5\nType Here:\t").upper()
        if al == "A":
            print("This Program Presents the simplest function in python which is the Print Function\n")
            activity1()
        elif al == "B":
            print("Input function action\n")
            activity2()
        elif al == "C":
            print("\n")
            activity3()
        elif al == "D":
            print("Use of the Length Function\n")
            activity4()
        elif al == "E":
            print("Simple math using variables to show age based on birth\n")
            activity5()
        else:
            print("Please Select within the options")
    elif sel == "B":
        al = input("\n\nSelected Section B:\nA - Activity 6\nB - Activity 7\nC - Activity 8\nD - Activity 9\nE - Activity 10\nType Here:\t").upper()
        if al == "A":
            print("Elementary Maths\n")
            activity6()
        elif al == "B":
            print("Live addition without needing to recall variable\n")
            activity7()
        elif al == "C":
            print("true or false statements with numbers\n")
            activity8()
        elif al == "D":
            print("true or false statements with strings\n")
            activity9()
        elif al == "E":
            print("fair counter using conditional statements\n")
            activity10()
        else:
            print("Please Select within the options")
    elif sel == "C":
        al = input("\n\nSelected Section C:\nA - Activity 11\nB - Activity 12\nC - Activity 13\nD - Activity 14\nE - Activity 15\nType Here:\t").upper()
        if al == "A":
            print("Temperature Determinator with Conditional statements and Elif function\n")
            activity11()
        elif al == "B":
            print("application of the for loop function\n")
            activity12()
        elif al == "C":
            print("use for loops to ask user 10 numbers and add the sum\n")
            activity13()
        elif al == "D":
            print("\n")
            activity14()
        elif al == "E":
            print("\n")
            activity15()
        else:
            print("Please Select within the options")
    elif sel == "D":
        al = input("\n\nSelected Section D:\nA - Activity 16\nB - Activity 17\nC - Activity 18\nD - Activity 19\nE - Activity 20\nType Here:\t").upper()
        if al == "A":
            print("\n")
            activity16()
        elif al == "B":
            print("\n")
            activity17()
        elif al == "C":
            print("\n")
            activity18()
        elif al == "D":
            print("\n")
            activity19()
        elif al == "E":
            print("\n")
            activity20()
        else:
            print("Please Select within the options")
    elif sel == "E":
        al = input("\n\nSelected Section E:\nA - Activity 21\nB - Activity 22\nC - Activity 23\nD - Activity 24\nType Here:\t").upper()
        if al == "A":
            print("\n")
            activity21()
        elif al == "B":
            print("\n")
            activity22()
        elif al == "C":
            print("\n")
            activity23()
        elif al == "D":
            print("\n")
            activity24()
        else:
            print("Please Select within the options")
    elif sel == "Exit":
        break
    else: 
        print("Please Select within the options")


