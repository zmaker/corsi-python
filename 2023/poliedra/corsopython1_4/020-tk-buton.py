import tkinter as tk

def clic(event):
    print("clic!")
    
def clic2():
    print("clic 2!")

app = tk.Tk()
app.title("Button")
app.geometry("300x200")

bt = tk.Button(text="Press me!")
bt.pack()
bt.bind("<Button-1>", clic)

bt2 = tk.Button(text="Clic me!", command=clic2)
bt2.pack()

app.mainloop()