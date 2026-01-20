import tkinter as tk

def hello():
    print("ciao")

win = tk.Tk()
win.geometry("300x200")
bt = tk.Button(text="Click", command=hello)
bt.pack()
win.mainloop()