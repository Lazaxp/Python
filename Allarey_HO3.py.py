import tkinter as tk 
 
mwindw = tk.Tk()

def add():
    number = entry1.get()
    number2 = entry2.get() 
    answer = int(number) + int(number2)
    top_label['text'] = f"The Sum of {number} + {number2} is: {answer}"
def multi():
    number = entry1.get()
    number2 = entry2.get() 
    answer = int(number) * int(number2)
    top_label['text'] = f"The Product of {number} x {number2} is: {answer}"
def subtract():
    number = entry1.get()
    number2 = entry2.get() 
    answer = int(number) - int(number2)
    top_label['text'] = f"The Difference of {number} - {number2} is: {answer}"
def divide():
    number = entry1.get()
    number2 = entry2.get() 
    answer = int(number) / int(number2)
    top_label['text'] = f"The Quotient of {number} / {number2} is: {answer}"

mwindw.title("Simulate Calculator")
mwindw.resizable(True, True)
mwindw.geometry("400x250")

top_label = tk.Label(mwindw, text = "Calculator", font = "Arial 15 bold")
top_label.pack(pady=10)

main_frame = tk.Frame(mwindw, width=1080, height=700, bg = "light blue", bd = 10)
main_frame.pack()

firstno = tk.Label(main_frame, text = "Enter 1st Number:", width=14)
firstno.grid(row = 0, column = 0, columnspan= 1, pady= 5, padx=2)
entry1 = tk.Entry(main_frame)
entry1.grid(row = 0, column= 3,pady= 5)

secondno = tk.Label(main_frame, text = "Enter 2nd Number:", width=14)
secondno.grid(row = 1, column = 0, columnspan= 1,pady= 5, padx=2)
entry2 = tk.Entry(main_frame)
entry2.grid(row = 1, column= 3,pady= 5)

button1 = tk.Button(main_frame, text = "Add", command = add, width=7)
button1.grid(row = 2, column = 0, columnspan=1,pady= 5)
button2 = tk.Button(main_frame, text = "Multiply", command = multi, width=7)
button2.grid(row = 3, column = 0, columnspan=1,pady= 5)
button3 = tk.Button(main_frame,text = "Subtract", command = subtract, width=7)
button3.grid(row = 2, column = 2, columnspan=3,pady= 5)
button4 = tk.Button(main_frame, text = "Division", command = divide, width=7)
button4.grid(row = 3, column = 2, columnspan=3,pady= 5)

def on_enter(event):
    button1['bg'] = "grey"
    
button1.bind("<Enter>", on_enter)

def on_leave(event):
    button1['bg'] = "light gray"
button1.bind("<Leave>", on_leave)

def on_enter(event):
    button2['bg'] = "grey"
button2.bind("<Enter>", on_enter)

def on_leave(event):
    button2['bg'] = "light gray"
button2.bind("<Leave>", on_leave)

def on_enter(event):
    button3['bg'] = "grey"
button3.bind("<Enter>", on_enter)

def on_leave(event):
    button3['bg'] = "light gray"
button3.bind("<Leave>", on_leave)

def on_enter(event):
    button4['bg'] = "grey"
button4.bind("<Enter>", on_enter)

def on_leave(event):
    button4['bg'] = "light gray"
button4.bind("<Leave>", on_leave)

mwindw.mainloop()