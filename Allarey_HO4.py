import tkinter as ui

mainw = ui.Tk()
 
mainw.title("Hands On 4 - Profile Builder")
mainw.geometry("900x420")
mainw.resizable(False, False)
mainw.configure(bg = "light grey")

def change_color():
    date = entry4.get()
    age = 2026 - int(date)
    label5['text'] = f"You are {age} years old." 
    u = entry1.get()
    m = entry2.get()
    a = entry3.get()
    if radioval == 1:
        gen = "Male"
        mainw['bg'] = "Blue"
        top_label['bg'] = "Blue"
    else:
        gen = "Female"
        mainw['bg'] = "Pink"
        top_label['bg'] = "Pink"
    userinfo = ui.Toplevel()
    userinfo.title("User Information")
    userinfo.geometry("300x400")
    userinfo.resizable(False, False)
    userinfo.configure(bg = "light grey")

    top_label1 = ui.Label(userinfo, text = "Student ID", font = "Century 30 bold", bg = "light grey")
    top_label1.pack()


    frame1 = ui.Frame(userinfo, bg = "white", bd = 10, width = 280, height = 320)
    frame1.pack()

    username = ui.Label(frame1, text = f"{u} {m} {a}", font = "Arial 20")
    username.pack()
    age1 = ui.Label(frame1, text = f"{age}", font = "Arial 20")
    age1.pack()
    gender = ui.Label(frame1, text = f"{gen}", font = "Arial 20")
    gender.pack()
top_label = ui.Label(mainw, text = "Profile Builder", font = "Century 30 bold", bg = "light grey")
top_label.pack()

frame0 = ui.Frame(mainw, bg = "white", bd = 10, width = 820, height = 250)
frame0.pack()

entry1 = ui.Entry(frame0, width = 40, bd = 3)
entry1.place(x = 10, y = 10)
label1 = ui.Label(frame0, text = "First Name", font = "Arial 10", bg = "white")
label1.place(x = 95, y = 31)
entry2 = ui.Entry(frame0, width = 40, bd = 3)
entry2.place(x = 280, y = 10)
label2 = ui.Label(frame0, text = "Middle Name", font = "Arial 10", bg = "white")
label2.place(x = 280+85, y = 31)
entry3 = ui.Entry(frame0, width = 40, bd = 3)
entry3.place(x = 280+85+185, y = 10)
label3 = ui.Label(frame0, text = "Last Name", font = "Arial 10", bg = "white")
label3.place(x = 280+85+185+85, y = 31)
entry4 = ui.Entry(frame0, width = 40, bd = 3)
entry4.place(x = 10, y = 80)
label4 = ui.Label(frame0, text = "Birth Year", font = "Arial 10", bg = "white")
label4.place(x = 95, y = 101)

label5 = ui.Label(frame0, text = "Computing Age...", font = "Arial 25 bold", bg = "white")
label5.place(x = 395-20+10, y = 101-20-10)

label6 = ui.Label(frame0, text = "Gender", font = "Arial 10", bg = "white")
label6.place(x = 100, y = 171-30)

radioval = ui.IntVar()
radiobutton0 = ui.Radiobutton(frame0,text = "Male", bg = "white", font = "Arial 10", value = 1)
radiobutton0.place(x = 280, y = 171-30)
radiobutton1 = ui.Radiobutton(frame0,text = "Female", bg = "white", font = "Arial 10", value = 0)
radiobutton1.place(x = 280+100, y = 171-30)

button0 = ui.Button(mainw, text = "Submit", font = "Arial 20", command = change_color)
button0.pack(pady = 20)
mainw.mainloop()