import tkinter as ui


main_tab = ui.Tk()
main_tab.title("Allarey HO Exam")
def registry():
    registry_tab = ui.Toplevel(main_tab)
    registry_tab.configure(bg = "white")
    registry_tab.title("Register an Account")
    def success():
        global username, userpassword
        userpassword = password_entry.get()
        if len(userpassword) >= 8:
            username = username_entry.get()
            registry_tab_frame["bg"] = "green"
            register_label["text"] = "You have Successfully Registered"
            register_label["font"] = "consolas 10 bold"
            registry_tab.destroy()
        else:
            register_label["text"] = "Password too short"
            register_label["font"] = "consolas 10 bold"            
    def see_pass():
        check = check_value.get()
        if check == 1:
            password_entry["show"] = ""
        if check == 0:
            password_entry["show"] = "*"

    register_label = ui.Label(registry_tab, text = "Register", font = "consolas 20 bold", anchor = "center", bg = "green", fg = "white")
    register_label.pack()

    registry_tab_frame = ui.Frame(registry_tab, bd = 5, bg = "white", width = 15)
    registry_tab_frame.pack()

    username_label = ui.Label(registry_tab_frame, text = "Username:", bg = "green", fg = "white")
    username_label.grid(row = 0, column = 0)
    username_entry = ui.Entry(registry_tab_frame, width = 20)
    username_entry.grid(row = 0, column = 1, columnspan = 2)

    password_label = ui.Label(registry_tab_frame, text = "Password:", bg = "green", fg = "white")
    password_label.grid(row = 1, column = 0, pady = 2)
    password_entry = ui.Entry(registry_tab_frame, width = 20, show = "*")
    password_entry.grid(row = 1, column = 1, columnspan = 2, pady = 2)

    check_value = ui.IntVar()
    see_password_button = ui.Checkbutton(registry_tab_frame, text = "See Password", variable = check_value, onvalue = 1, offvalue = 0, command = see_pass)
    see_password_button.grid(row = 2, column = 0, pady = 2, columnspan=3)

    register_button = ui.Button(registry_tab_frame, text = "Register", command = success)
    register_button.grid(row = 3, column = 0, columnspan=3)

def log_in():
    login_tab = ui.Toplevel(main_tab)
    login_tab.configure(bg = "white")
    login_tab.title("Log into an Account")

    def success():
        user = username_entry.get()
        password = password_entry.get()
        if user == username:
            if password == userpassword:
                login_tab_frame["bg"] = "green"
                login_label
                login_label["text"] = "Log in Successful"
                login_label["font"] = "consolas 10 bold"
            else:
                login_tab_frame["bg"] = "red"
                username_label["bg"] = "red"
                password_label["bg"] = "red"
                login_label["text"] = "Your user credentials are incorrect!"
                login_label["font"] = "consolas 10 bold"  
        else:
            username_label["bg"] = "red"
            password_label["bg"] = "red"
            login_tab_frame["bg"] = "red"
            login_label["text"] = "Your user credentials are incorrect!"
            login_label["font"] = "consolas 10 bold"   
                     
    def see_pass():
        check = check_value.get()
        if check == 1:
            password_entry["show"] = ""
        if check == 0:
            password_entry["show"] = "*"

    login_label = ui.Label(login_tab, text = "Log In", font = "consolas 20 bold", anchor = "center", bg = "green", fg = "white")
    login_label.pack() 

    login_tab_frame = ui.Frame(login_tab, bd = 5, bg = "white", width = 15)
    login_tab_frame.pack()

    username_label = ui.Label(login_tab_frame, text = "Username:", bg = "green", fg = "white")
    username_label.grid(row = 0, column = 0)
    username_entry = ui.Entry(login_tab_frame, width = 20)
    username_entry.grid(row = 0, column = 1, columnspan = 2)

    password_label = ui.Label(login_tab_frame, text = "Password:", bg = "green", fg = "white")
    password_label.grid(row = 1, column = 0, pady = 2)
    password_entry = ui.Entry(login_tab_frame, width = 20, show = "*")
    password_entry.grid(row = 1, column = 1, columnspan = 2, pady = 2)
   
    check_value = ui.IntVar()
    see_password_button = ui.Checkbutton(login_tab_frame, text = "See Password", variable = check_value, onvalue = 1, offvalue = 0, command = see_pass)
    see_password_button.grid(row = 2, column = 0, pady = 2, columnspan=3)

    login_button = ui.Button(login_tab_frame, text = "Log in", command = success)
    login_button.grid(row = 3, column = 0, columnspan=3)
welcome_label = ui.Label(main_tab,text = "Welcome!", font = "consolas 25 bold", width = 30, anchor = "center")
welcome_label.pack()

main_tab_frame = ui.Frame(main_tab, bd = 5)
main_tab_frame.pack()

register_button = ui.Button(main_tab_frame, text = "Register", width = 25, bg = "green", command = registry)
register_button.pack(pady = 10)
Log_button = ui.Button(main_tab_frame, text = "Log In", width = 25, bg = "white", command = log_in)
Log_button.pack(pady = 10)


main_tab.mainloop()
