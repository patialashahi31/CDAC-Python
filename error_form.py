import tkinter as tk
from registration_Form import *
from mysql.connector import connection
from mysql.connector import Error
from tkinter import messagebox

class XGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gui")
        self.master.geometry('400x400')

        self.createWi()

    def createWi(self):
        self.lab = tk.Label(text="Account not registered", font="Arial 20" , fg='red')
        self.lab.place(x=80,y=100)
        self.reg = tk.Button(self.master, text="Register", fg="white", bg="#4285F4")
        self.reg.bind("<1>", self.regg)
        self.reg.place(x=200, y=250)


    def regg(self,event):
        self.master.destroy()
        app2 = MyGui(tk.Tk())




