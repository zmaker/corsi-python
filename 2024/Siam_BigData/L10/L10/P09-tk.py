import tkinter as tk

def hello():
    print("ciao")

win = tk.Tk()
win.geometry("300x200")
button = tk.Button(text="Click me", command=hello)
button.pack()
win.mainloop()
