import tkinter as tk

app = tk.Tk()
app.title("my App")
app.geometry("300x200")

lb1 = tk.Label(app)
lb1['text'] = 'label 1'
lb1['background'] = '#fdffc7'
lb1.pack(fill=tk.BOTH)

lb2 = tk.Label(app)
lb2['text'] = 'label 2'
lb2['background'] = '#c7f9ff'
lb2.pack(side=tk.LEFT, padx=5, pady=5)

lb3 = tk.Label(app)
lb3['text'] = 'label 3'
lb3['background'] = '#d3ffc7'
lb3.pack()

app.mainloop()
print("end app")
