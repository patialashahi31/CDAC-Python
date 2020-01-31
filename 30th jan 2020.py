from threading import Thread
import time
class A(Thread):
    def __init__(self,name):
        Thread.__init__(self,name = name)
    def run(self):
        fruits = ['apple','banana','pineapple','orange','strawberry','grapes','mango','blackberry','dates','peach']
        for i in fruits:
            print(f"Fruit this time {i}")
            time.sleep(1)

class B(Thread):
    def __init__(self,name):
        Thread.__init__(self,name = name)
    def run(self):
        alphabets = ['a','b','c','d','e','f','g','h','i','j']
        for i in alphabets:
            print(f"Alphabet this time {i}")
            time.sleep(1)

process1 = A("Fruits")
process1.start()
process2 = B("Alphabets")
process2.start()

for i in range(10):
    print(i)
    time.sleep(2)







