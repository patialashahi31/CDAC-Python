from tkinter import filedialog
from tkinter import *
class MyFourthGui(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui Page")

        self.createWidgets()

    def createWidgets(self):

        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        self.fileMenu = Menu(self.menubar)

        self.submenu = Menu(self.fileMenu)
        self.submenu.add_command(label="Open",command=self.options)
        self.submenu.add_command(label="Exit",command=self.exits)
        self.fileMenu.add_cascade(label='Options', menu=self.submenu)

        self.fileMenu.add_separator()

        self.menubar.add_cascade(label="File", menu=self.fileMenu)

    def exits(self):
        exit()

    def options(self):
        s = filedialog.askopenfilenames()




def main():
    root = Tk()

    app = MyFourthGui(master=root)

    app.mainloop()

if __name__ == '__main__':
    main()