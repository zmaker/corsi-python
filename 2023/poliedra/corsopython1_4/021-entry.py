import tkinter as tk

def clic(event):
    str1 = msg.get()
    print(str1)
    msg.delete(0, tk.END)
    msg.insert(0, "Ciao!")

win = tk.Tk()
win.title("Entry example")
win.geometry("300x200")

bt = tk.Button(text="Press me")
bt.pack()
bt.bind("<Button-1>", clic)

msg = tk.Entry(width=50)
msg.pack()

win.mainloop()
print("end")


