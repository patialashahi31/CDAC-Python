
class Student:

    def __init__(self,name,n,s=[],t=0,avgs=0):
        self.name = name
        self.n = n
        self.s= s
        self.t=t
        self.avgs=avgs


    def setscores(self,s):
        self.s = s

    def getscores(self):
        return self.s

    def settotal(self,t):

        self.t = t


    def getTotal(self):

        return self.t

    def setavg(self,avgs):

        self.avgs = avgs

    def getavg(self):

        return self.avgs

    def getName(self):
        return self.name



    def inputMarks(self):
        scores = []
        print(f"Enter {self.n} marks ")
        for i in range(self.n):
            y = int(input(f"Enter {i+1} value"))
            scores.append(y)

        self.setscores(scores)
        print(scores)
        print(self.getscores())

    def totalScores(self):
        m = self.getscores()
        sumx = sum(m)
        self.settotal(sumx)




    def avgScore(self):
        totalx = self.getTotal()
        avgs = (totalx/(self.n))
        self.setavg(avgs)
        print(self.getavg())


    def __str__(self):
        return f'{self.getName()} got {self.getName()}= {self.getTotal()}/{self.n*100}'



    def displayTotal(self):
        self.totalScores()
        print(f"Total scores of {self.getName()}= {self.getTotal()}/{self.n * 100}")

    def displayAvg(self):
        self.avgScore()
        print(f'Average score of {self.getName()} = {self.getavg()} ')


name1 = input("Enter name of first student")
numberOfSubjects = int(input("Enter number of subjects"))
first = Student(name1,numberOfSubjects)
print(first.getName())

first.inputMarks()

first.displayTotal()

first.displayAvg()


first.__str__()



