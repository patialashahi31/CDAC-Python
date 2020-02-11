import tkinter as tk
class MyThirdGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui Page")

        self.createWidgets()

    def createWidgets(self):
        self.colors = ["red","green","blue"]

        r=0

        for c in self.colors:
            self.lb1 = tk.Label(self.master,text=self.colors[r])
            self.lb1.grid(row=r,column=0)
            self.ent = tk.Entry(bg=c)
            self.ent.grid(row=r,column=1)
            r = r+1




def main():
    root = tk.Tk()
    root.geometry("200x200")
    app = MyThirdGui(master=root)

    app.mainloop()

if __name__ == '__main__':
    main()