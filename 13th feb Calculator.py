import tkinter as tk

class MyGui(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.createWidgets()

    x=""
    res=0
    l = []
    reslist = []
    def createWidgets(self):
        self.divide = tk.Button(self.master, text="/", width=5, height=2,command=self.div)
        self.mutiply = tk.Button(self.master, text="*", width=5, height=2,command=self.mul)
        self.minus = tk.Button(self.master, text="-", width=5, height=2,command=self.min)
        self.add = tk.Button(self.master, text="+", width=5, height=2,command=self.plus)
        self.input = tk.Entry(self.master,width=30)
        self.input.place(x=30,y=10)

        self.one = tk.Button(self.master,text="1",width=5,height=2,command=self.n1)
        self.two = tk.Button(self.master, text="2",width=5,height=2,command=self.n2)
        self.third = tk.Button(self.master, text="3",width=5,height=2,command=self.n3)
        self.one.place(x=30,y=70)
        self.two.place(x=90, y=70)
        self.third.place(x=150, y=70)

        self.four = tk.Button(self.master, text="4",width=5,height=2,command=self.n4)
        self.five = tk.Button(self.master, text="5",width=5,height=2,command=self.n5)
        self.six = tk.Button(self.master, text="6",width=5,height=2,command=self.n6)
        self.four.place(x=30, y=120)
        self.five.place(x=90, y=120)
        self.six.place(x=150, y=120)

        self.divide.place(x=210, y=70)
        self.seven = tk.Button(self.master, text="7",width=5,height=2,command=self.n7)
        self.eight = tk.Button(self.master, text="8",width=5,height=2,command=self.n8)
        self.nine = tk.Button(self.master, text="9",width=5,height=2,command=self.n9)
        self.seven.place(x=30, y=170)
        self.mutiply.place(x=210, y=120)
        self.eight.place(x=90, y=170)
        self.nine.place(x=150, y=170)

        self.zero = tk.Button(self.master, text="0",width=5,height=2,command=self.n0)
        self.back = tk.Button(self.master, text="<--",width=5,height=2,command=self.b)
        self.clear = tk.Button(self.master, text="C",width=5,height=2,command=self.cl)
        self.zero.place(x=30, y=220)
        self.minus.place(x=210, y=170)
        self.back.place(x=90, y=220)
        self.clear.place(x=150, y=220)


        self.add.place(x=210, y=220)
        self.equal = tk.Button(self.master, text="=",width=5,height=12,bg="yellow")
        self.equal.place(x=270,y=70)

        self.equal.bind("<1>",self.logic1)

    def logic1(self,event):
        if(self.l[-1]=="+"):
            self.plus()
        elif(self.l[-1]=="-"):
            self.min()
        elif(self.l[-1]=="/"):
            self.div()
        elif(self.l[-1]=="*"):
            self.mul()
        self.input.delete(0, tk.END)
        self.input.insert(0, self.reslist[-1])

    def n1(self):

        self.x += "1"
        self.input.delete(0,tk.END)
        self.input.insert(0,self.x)

    def n2(self):

        self.x += "2"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n3(self):

        self.x += "3"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n4(self):

        self.x += "4"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n5(self):

        self.x += "5"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n6(self):

        self.x += "6"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n7(self):

        self.x += "7"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n8(self):

        self.x += "8"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n9(self):

        self.x += "9"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def n0(self):

        self.x += "0"
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)

    def plus(self):
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)
        self.input.delete(0, tk.END)




        if(len(self.reslist)==0):
            self.reslist.append(int(self.x))
            self.l += ['+']


            print(self.reslist)
        else:
            if (self.l[-1] == "+"):
                self.reslist.append(self.reslist[-1] + int(self.x))
            elif (self.l[-1] == "-"):
                self.reslist.append(self.reslist[-1] - int(self.x))

            elif (self.l[-1] == "/"):
                self.reslist.append(self.reslist[-1] / int(self.x))
            elif (self.l[-1] == "*"):
                self.reslist.append(self.reslist[-1] * int(self.x))


            self.l += ['+']

            print(self.reslist)

        self.x=""


    def b(self):
        y =  self.x[0:len(self.x)-1]
        self.x = self.x + "\b"
        self.input.delete(0, tk.END)
        self.input.insert(0, y)

        print(self.x)

    def cl(self):
        self.x=""
        self.reslist=[]
        self.l = []
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)


    def mul(self):
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)
        self.input.delete(0, tk.END)




        if (len(self.reslist) == 0):
            self.reslist.append(int(self.x))
            print(self.reslist)
            self.l += ['*']

        else:
            if (self.l[-1] == "+"):
                self.reslist.append(self.reslist[-1] + int(self.x))
            elif (self.l[-1] == "-"):
                self.reslist.append(self.reslist[-1] - int(self.x))

            elif (self.l[-1] == "/"):
                self.reslist.append(self.reslist[-1] / int(self.x))
            elif (self.l[-1] == "*"):
                self.reslist.append(self.reslist[-1] * int(self.x))



            print(self.reslist)
            self.l += ['*']


        self.x = ""

    def div(self):
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)
        self.input.delete(0, tk.END)



        if (len(self.reslist) == 0):
            self.reslist.append(int(self.x))
            print(self.reslist)
            self.l += ['/']

        else:
            if (self.l[-1] == "+"):
                self.reslist.append(self.reslist[-1] + int(self.x))
            elif (self.l[-1] == "-"):
                self.reslist.append(self.reslist[-1] - int(self.x))

            elif (self.l[-1] == "/"):
                self.reslist.append(self.reslist[-1] / int(self.x))
            elif (self.l[-1] == "*"):
                self.reslist.append(self.reslist[-1] * int(self.x))



            self.l += ['/']

            print(self.reslist)
        self.x = ""

    def min(self):
        self.input.delete(0, tk.END)
        self.input.insert(0, self.x)
        self.input.delete(0, tk.END)



        if (len(self.reslist) == 0):
            self.reslist.append(int(self.x))


            print(self.reslist)
            self.l += ['-']

        else:
            if (self.l[-1] == "+"):
                self.reslist.append(self.reslist[-1] + int(self.x))
            elif (self.l[-1] == "-"):
                self.reslist.append(self.reslist[-1] - int(self.x))

            elif (self.l[-1] == "/"):
                self.reslist.append(self.reslist[-1] / int(self.x))
            elif (self.l[-1] == "*"):
                self.reslist.append(self.reslist[-1] * int(self.x))
            self.l += ['-']

            print(self.reslist)
        self.x = ""


def main():
    root = tk.Tk()
    root.geometry("350x300")
    app = MyGui(master=root)

    app.mainloop()

if __name__ == '__main__':
    main()