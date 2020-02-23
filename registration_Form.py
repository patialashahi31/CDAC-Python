import tkinter as tk
from mysql.connector import connection
from mysql.connector import Error
from tkinter import messagebox


class MyGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui Page")
        self.master.geometry("500x500")
        self.createWidgets()

    def createWidgets(self):
        self.lab1 = tk.Label(self.master, text="REGISTER", bg="#FBBC05", fg="red", font="Arial 30")
        self.lab1.place(x=127, y=20)
        self.userNameLabel = tk.Label(self.master, text="Name", bg="black", fg="white", font="Arial 12"
                                                                                                "")
        self.userNameLabel.place(x=30, y=80)
        self.pwdLabel = tk.Label(self.master, text="Password", bg="black", fg="white", font="Arial 12")
        self.pwdLabel.place(x=30, y=140)
        self.ask = tk.Label(self.master, text="Rank", bg="black", fg="white", font="Arial 12")
        self.ask.place(x=30, y=200)
        self.userNameTf = tk.Entry(self.master)
        self.userNameTf.place(x=180, y=80)
        self.pwdTf = tk.Entry(self.master, show="*")
        self.pwdTf.place(x=180, y=140)
        self.var = tk.IntVar()
        self.askTf1 = tk.Radiobutton(self.master,text="Student",variable=self.var,value=1)
        self.askTf2 = tk.Radiobutton(self.master, text="Employee", variable=self.var, value=2)
        self.askTf1.place(x=180,y=190)
        self.askTf2.place(x=180, y=220)


        self.red = tk.Label(self.master, text="Password must contain 6-12 characters", fg="red")
        self.red.place(x=180, y=170)
        self.reg = tk.Button(self.master, text="Register", fg="white", bg="#4285F4",command=self.show)
        self.reg.place(x=200, y=350)


        self.var1 = tk.StringVar()
        self.option = tk.OptionMenu(self.master,self.var1,"A","B","C")
        self.var1.set("Select")
        self.grade = tk.Label(self.master,text="Grade",bg="black", fg="white", font="Arial 12")
        self.grade.place(x=30,y=250)
        self.option.place(x=180,y=250)

    def show(self):

        username = self.userNameTf.get()
        pwd = self.pwdTf.get()
        y=""
        z = self.var1.get()
        ranks = self.var.get()
        if(ranks==1):
            y += "Student"
        else:
            y += "Employee"
        try:
            db = connection.MySQLConnection(host="localhost", database="db", user="root", password="root",
                                                charset="utf8")
            if db.is_connected() and (len(pwd)>=6 and len(pwd)<=12):
                s = f"insert into users(id,username,password,grade,rank) values(null,'{username}','{pwd}','{z}','{y}')"

                c = db.cursor()
                c.execute(s)
                db.commit()

                messagebox.showinfo("Continue", "Ok")

            else:
                messagebox.showerror("Error","Password must be 6 to 12 characters long")


        except Error as e:
            print(e)

        finally:
            db.close()



