import tkinter as tk

def saluta():
    print("ciao")

win = tk.Tk()

label = tk.Label(text="Hello")
label.pack()

bt = tk.Button(text="Clic me", command=saluta)
bt.pack()

win.title("Prima App Tk")
win.geometry("300x200")

win.mainloop()