import os
records = {}
while True:
    print("Welcome to Student Record Program - Select from the Options Below:\n\n")
    print("Add - Add Info\nSearch - Search Info\nDel - Delete a Record\nMod - Modify Recored\nAll - Show all current Records\nExp - Export Data")
    res = input("Type here:\t").capitalize()
    os.system("cls")
    if res == "Add":
        
        print("- Add a your Students Info -\n")
        code = input("Input Student Key:\t")
        records[code] = []
        fname = input("Input Student First Name:\t").upper()
        lname = input("Input Student Last Name:\t").upper()
        course = input("Input Student Course:\t").upper()
        email = input("Input Student Email Address:\t").upper()
        if "@gmail.com" in email:
            continue
        else:
            print("Invalid Email")
        os.system("cls")
        records = {code :[fname, lname, course, email]}
        print("Data has been Recorded.")
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
            print("Input new Student Record")
            code = input("Input Student Key:\t")
            records.pop(key)
            records[code] = []
            fname = input("Input Student First Name:\t").upper()
            lname = input("Input Student Last Name:\t").upper()
            course = input("Input Student Course:\t").upper()
            email = input("Input Student Email Address:\t").upper()
            if "@gmail.com" in email:
                continue
            else:
                print("Invalid Email")
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
    elif res == "Exp":
        print("- Export Record -")
    else:
        os.system("cls")
        print("\nPlease Select within the Options.\n")
