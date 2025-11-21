import os, json
records = {}
while True:
    print("Welcome to Student Record Program - Select from the Options Below:\n\n")
    print("Add - Add Info\nSrh - Search Info\nDel - Delete a Record\nMod - Modify Recored\nAll - Show all current Records\nExp - Export Data")
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
        if "@" in email:
            continue
        else:
            print("Invalid Email")
        os.system("cls")
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
