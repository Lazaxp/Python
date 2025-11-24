from activity25_1 import *
name = input("Hi, Whats your Name?:\t").capitalize()
while True:
    print(f"\n\nWelcome {name} to my Code Compiler.\nSelect a program section you want to run:")
    sel = input("A - Activity 1-5\nB - Activity 6-10\nC - Activity 11-15\nD - Activity 16-20\nE - Activity 21-24\nF - Code Challenge 1-15\nType Here:\t").upper()
    if sel == "A":
        al = input("\n\nSelected Section A:\nA - Activity 1\nB - Activity 2\nType Here:\t").upper()
        if al == "A":
            print("This Program Presents the simplest function in python which is the Print Function\n")
            activity1()
        elif al == "B":
            print("\n")
            activity2()
        elif al == "C":
            print("\n")
            activity3()
        elif al == "D":
            print("\n")
            activity4()
        elif al == "E":
            print("\n")
            activity5()
        else:
            print("Please Select within the options")
    elif sel == "B":
        al = input("\n\nSelected Section B:\nA - Activity 6\nB - Activity 7\nC - Activity 8\nD - Activity 9\nE - Activity 10\nType Here:\t").upper()
        if al == "A":
            print("\n")
            activity6()
        elif al == "B":
            print("\n")
            activity7()
        elif al == "C":
            print("\n")
            activity8()
        elif al == "D":
            print("\n")
            activity9()
        elif al == "E":
            print("\n")
            activity10()
        else:
            print("Please Select within the options")
    elif sel == "Exit":
        break
    else: 
        print("Please Select within the options")
