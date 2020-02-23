ux = "Welcome "
import tkinter as tk
from registration_Form import *
from mysql.connector import connection
from mysql.connector import Error
from tkinter import messagebox
from error_form import *


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
        user = self.userNameTf.get()
        print("Password - " + str(self.pwdTf.get()))
        pas = self.pwdTf.get()
        try:
            db = connection.MySQLConnection(host="localhost", database="db", user="root", password="root",
                                            charset="utf8")
            if db.is_connected():
                s = "select * from users"

                c = db.cursor()
                c.execute(s)
                data = c.fetchall()
                flag=1
                for row in data:
                    username = row[1]
                    pasword = row[2]
                    if(username==user and pas==pasword):
                        print("Account verified")
                        global ux

                        change(username)
                        self.master.destroy()

                        app4 = XiGui(tk.Tk())

                        flag=0
                        break

                if(flag==1):
                    print("Not verified")
                    self.master.destroy()
                    app3 = XGui(tk.Tk())


            else:
                print("Not connected")

        except Error as e:
            print(e)

        finally:
            db.close()




    def registeruser(self,event):
        self.master.destroy()
        app2 = MyGui(tk.Tk())

def change(value):
    global ux
    ux += value


class XiGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui ")
        self.master.geometry('400x400')


        self.createWidget()

    def createWidget(self):

        self.v = tk.StringVar()
        self.v.set(ux)
        print(self.v.get())
        self.lab = tk.Label(master=self.master,textvariable=self.v, font="Arial 20" , fg='red')

        self.lab.place(x=80,y=100)





    def regg(self,event):
        self.master.destroy()
        app2 = MyGui(tk.Tk())
def main():
    root = tk.Tk()
    root.geometry("400x400")
    app = MySecondGui(master=root)

    app.mainloop()

if __name__ == '__main__':
    main()