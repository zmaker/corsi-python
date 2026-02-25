import tkinter as tk

def clic():
    s = msg.get()
    print(s)
    msg.delete(0, tk.END)
    msg.insert(0, "Ciao")

app = tk.Tk()
app.title("my App")
app.geometry("300x200")

bt = tk.Button(text="saluto", command=clic)
bt.pack()

msg = tk.Entry(width=50)
msg.pack()

app.mainloop()
print("end app")
