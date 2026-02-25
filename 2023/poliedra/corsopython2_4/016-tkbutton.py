import tkinter as tk

def btClicked():
    print("clic")
    
def btPressed(event):
    print("pressed")
    print(event)

app = tk.Tk()
app.title("Clic App")
app.geometry("300x200")

bt = tk.Button(text="clic me", command=btClicked)
bt.pack()

bt2 = tk.Button(text="Press me")
bt2.pack()
bt2.bind('<Button-1>', btPressed)

app.mainloop()
print("end app")
