#Hands-on 2 ITCS103
import tkinter as tk

window = tk.Tk()
window.title("Student Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg = "light gray")
label = tk.Label(window, text = "STUDENT PROFILE", font = ("Arial Black", 30, "bold"), fg = "white" ,bg = "gray",  anchor = "center", width = 200)
label.pack()
label = tk.Label(window, text = "Name: Luis Angelo Z. Allarey", font = ("cosmic sans", 11, "bold"), fg = "gray",bg = "light gray",  anchor = "w", width = 200)
label.pack(padx = 1, pady=5)
label = tk.Label(window, text = "Course: BSIT", font = ("cosmic sans", 11, "bold"), fg = "white",bg = "gray",  anchor = "w", width = 200)
label.pack(pady=5)
label = tk.Label(window, text = "Birthday: November 6, 2006", font = ("cosmic sans", 11, "bold"), fg = "gray",bg = "light gray",  anchor = "w", width = 200)
label.pack(pady=5)
label = tk.Label(window, text = "Motto:", font = ("cosmic sans", 11, "bold"), fg = "white",bg = "gray",  anchor = "w", width = 200)
label.pack(pady=5)
label = tk.Label(window, text = "\"Any change is better than no change\"", font = ("mistral", 18), fg = "white",bg = "black",  anchor = "center")
label.pack(pady=5)

window.mainloop() 

