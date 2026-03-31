import tkinter as ui

main_tab = ui.Tk()
main_tab.title("Allarey HO Exam")

welcome_label = ui.Label(main_tab,text = "Welcome!", font = "consolas 25 bold", width = 30, anchor = "center")
welcome_label.pack()

main_tab_frame = ui.Frame(main_tab, bg = "white", bd = 5, relief = "solid")
main_tab_frame.pack()

register_button = ui.Button(main_tab_frame, text = "Register", width = 10, bg = )
main_tab.mainloop()