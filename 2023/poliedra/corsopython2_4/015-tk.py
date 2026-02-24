import tkinter as tk

app = tk.Tk()
app.title("my App")
app.geometry("300x200")

lb = tk.Label(text="Hello TK")
lb.pack()

app.mainloop()
print("end app")