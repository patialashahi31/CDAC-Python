import tkinter as tk
class MyFirstGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui Page")
        self.createLabel()

    def createLabel(self):
        self.val = tk.Label(self.master,text='Name')
        self.val.pack(side='left')
        x = tk.StringVar()
        self.input = tk.Entry(self.master,textvariable=x,bg='red')
        x.set("Hi")
        self.input.pack()
        self.rad1 = tk.Radiobutton(self.master,text="male",value=1)
        self.rad2 = tk.Radiobutton(self.master, text="female", value=2)
        self.rad1.pack()
        self.rad2.pack()
        self.check = tk.Checkbutton(self.master,text="Physics")
        self.check.pack(side='right')
        self.list = tk.Listbox(self.master)
        self.list.insert(tk.END,"select")
        a = ["Apple","Banana","Grapes"]
        for i in a:
            self.list.insert(tk.END,i)
        self.list.pack()
        self.msg = tk.Message(self.master, text='This is a long text from someone by someone', width=50)
        self.msg.pack()
        self.but = tk.Button(self.master,text = "Click",command = self.show,bg='green')
        self.but.pack()

    def show(self):
        self.lab = tk.Label(self.master,text="Hello")
        self.lab.pack()




def main():
    root = tk.Tk()
    app = MyFirstGui(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()

