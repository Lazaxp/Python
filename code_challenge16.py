import os
records = {}
while True:
    print("Welcome to Student Record Program - Select from the Options Below:\n\n")
    print("Add - Add Info\nSearch - Search Info\nDel - Delete a Record\nMod - Modify Recored")
    res = input("Type here:\t").capitalize()
    os.system("cls")
    if res == "Add":
        print("- Add a your Students Info -\n")
        code = input("Input Student Key:\t").upper()
        fname = input("Input Student First Name:\t").upper()
        lname = input("Input Student Last Name:\t").upper()
        course = input("Input Student Course:\t").upper()
        email = input("Input Student Emil Address:\t").upper()
        os.system("cls")
        records = {code: [fname, lname, course, email]}
        print("Data has been Recorded.")
    elif res == "Search":
        print("- Search Student Records - ")
        key = input("Input here your Student Key:\t").upper()
        os.system("cls")
        for x in records.keys():
            if key in records.keys():
                print("Record Found")
                for y in records[keys]:
                    print(y)
            else:
                print("Record Not Found")
    elif res == "Del" or res == "Delete":
        os.system("cls")
        print("- Delete Student Record -")
        for x in records.keys():
            print(records.keys())
