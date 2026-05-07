import os
while True:
    os.system("cls")
    print("=== Dream Files Manager ===")
    print("1.) Read Inspiring Messages\n2.) Add your Inspiring Message\n3.) Rewrite the File\n4.) Exit")

    option = int(input("Type here: "))

    if option == 1:
        with open("dreams.txt", "r") as file:
            content = file.read()
            print("=================================================================================\n")
            print(content)
            print("\n=================================================================================")
            move = input("Press Enter to Continue.")
            os.system("cls")
    elif option == 2:
        while True:
            file = open("dreams.txt", "a")
            new_message = input("\nType here for your new Inspiring Message: ")
            file.write(f"\n{new_message}")
            print("New Inspirations!:")
            with open("dreams.txt", "r") as file:
                content = file.read()
                print("=================================================================================\n")
                print(content)
                print("\n=================================================================================")
            cycle = input("\nContinue?(y/n): ")
            if cycle == "y":
                os.system("cls")
                continue
            elif cycle == "no":
                file.close()
                os.system("cls")
                break
            else:
                print("Please choose within the options.")
    elif option == 3:
        warning = input("WARNING, this will overwrite the entire file.\nContinue?(Yes/No): ").lower()
        if warning == "yes":
            file = open("dreams.txt", "w")
            new_message = input("\nType your new Inspiring Message here: ")
            file.write(new_message)
            file.close()
            print("New Inspirations!:")
            with open("dreams.txt", "r") as file:
                content = file.read()
                print("=================================================================================\n")
                print(content)
                print("\n=================================================================================")
                move = input("Press Enter to Continue.")
                os.system("cls")
        elif warning == "no":
            continue
        else:
           print("Please choose within the options.")
    elif option == 4:
        os.system("cls")
        print("\n\n=== Session ended. ===")
        break
    else:
        print("Please choose within the options.")