import tkinter as tk
class MySecondGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui Page")

        self.createWidgets()

    def createWidgets(self):
        self.spin1 = tk.Spinbox(self.master,from_=0,to=30)
        self.spin1.pack()
        self.spin2 = tk.Spinbox(self.master, values=(5,10,15))
        self.spin2.pack()
        var = tk.StringVar()
        var.set("Select.")
        self.option = tk.OptionMenu(self.master,var,"Patiala","Chandigarh")
        self.option.pack()
        print(var.get())
        self.tex = tk.Text(self.master,height=5,width=30)
        self.tex.insert(tk.END,"Just a new line\n with text\n Hi")
        self.tex.pack()
        self.scale1 = tk.Scale(self.master,from_=0,to=10)
        self.scale1.pack()
        self.scale2 = tk.Scale(self.master,from_=0,to=100,tickinterval=5,orient="horizontal",length=500)
        self.scale2.pack()
        self.can = tk.Canvas(self.master,bg="green",height=100,width=100)
        self.can.create_line(0,0,50,50)
        self.can.pack()

        self.can2 = tk.Canvas(self.master, bg="green", height=100, width=100)
        self.can2.pack()
        self.img = tk.PhotoImage(file="unnamed.png")
        self.can2.create_image(20,20,anchor=tk.NW,image=self.img)





def main():
    root = tk.Tk()

    app = MySecondGui(master=root)

    app.mainloop()

if __name__ == '__main__':
    main()
