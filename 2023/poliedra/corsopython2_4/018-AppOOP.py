import tkinter as tk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("OOP Win")
        self.geometry("300x200")
        
        self.label = tk.Label(self, text='OOP App!')
        self.label.pack()
        
        self.bt = tk.Button(self, text='Clic me')
        self.bt['command'] = self.bt_clicked
        self.bt.pack()
    
    def bt_clicked(self):
        print("hello")
        showinfo(title='Info', message="Hello! Click")
    

if __name__ == '__main__':
    app = App()
    app.mainloop()