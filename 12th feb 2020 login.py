import tkinter as tk
from registration_Form import *
class MySecondGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui Page")

        self.createWidgets()

    def createWidgets(self):
        self.lab1 = tk.Label(self.master,text="LOGIN",bg="#FBBC05",fg="red",font="Arial 30")
        self.lab1.place(x=127,y=20)
        self.userNameLabel = tk.Label(self.master,text="User ID" , bg= "black",fg="white",font="Arial 12"
                                                                                               "")
        self.userNameLabel.place(x=30,y=80)
        self.pwdLabel = tk.Label(self.master, text="Password", bg="black", fg="white", font="Arial 12")
        self.pwdLabel.place(x=30, y=140)
        self.userNameTf = tk.Entry(self.master)
        self.userNameTf.place(x=180,y=80)
        self.pwdTf = tk.Entry(self.master,show="*")
        self.pwdTf.place(x=180, y=140)
        self.red = tk.Label(self.master,text="Password must contain 6-12 characters",fg="red")
        self.red.place(x=180,y=180)
        self.signIn = tk.Button(self.master,text="Sign In",fg="white",bg="#34A853")
        self.signIn.bind("<1>",self.show)
        self.signIn.place(x=110,y=250)
        self.reg = tk.Button(self.master, text="Register", fg="white", bg="#4285F4")
        self.reg.bind("<1>", self.registeruser)
        self.reg.place(x=200, y=250)
        self.new = tk.Label(self.master)
        self.new.place(x=110,y=280)

    def show(self,event):
        print("Username - " + str(self.userNameTf.get()))
        print("Password - " + str(self.pwdTf.get()))

    def registeruser(self,event):
        self.master.destroy()
        app2 = MyGui(tk.Tk())


def main():
    root = tk.Tk()
    root.geometry("400x400")
    app = MySecondGui(master=root)

    app.mainloop()

if __name__ == '__main__':
    main()