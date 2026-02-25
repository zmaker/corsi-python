import tkinter as tk

win = tk.Tk()
win.title("la mia prima app")
win.geometry("400x300")

label = tk.Label(text="Hello Tkinter")
label.pack()

win.mainloop()
print("end")

