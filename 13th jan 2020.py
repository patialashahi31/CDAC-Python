def first():
    print("Enter number of integers")
    n = int(input())
    print("Enter values")
    l=[]
    for i in range(n):
        x = int(input())
        l.append(x)

    print(f"List of integers {l}" )


def second():
    print("Enter number of strings")
    n = int(input())
    print("Enter values")
    l = []
    for i in range(n):
        x = input()
        l.append(x)

    print(f"List of integers {l}")




def third():
    gadgets = ["mobile","laptop",100,"Camera",310.28,"Speakers",27.00,"Television",1000,"Laptop case","camera lens"]
    print("Create separate lists of strings and integers")
    integers =[]
    strings = []
    for i in range(len(gadgets)):
        x = str(gadgets[i])
        if x.isdigit()  :
            integers = integers + [int(x)]
        elif x.replace('.', '', 1).isdigit():
            integers = integers + [float(x)]
        else:
            strings = strings + [gadgets[i]]

    print(f'List of integers of floats {integers}')
    print(f'List of strings')
    print(f"sort the strings in ascending order {sorted(strings)}")
    print(f"sort the strings in descending order {sorted(strings,reverse=True)}")
    print(f"sort numbers in ascending order {sorted(integers)}")
    print(f"sort the strings in descending order {sorted(integers, reverse=True)}")

import math
def fourth():
    sin =[]
    cos = []
    tan = []
    thirty = math.sin(math.radians(30))
    six = math.sin(math.radians(60))
    nine = math.sin(math.radians(90))
    sin += [float("{0:.2f}".format(round(thirty,2))),float("{0:.2f}".format(round(six,2))),float("{0:.2f}".format(round(nine,2)))]
    cos += [float("{0:.2f}".format(round(thirty,2))),float("{0:.2f}".format(round(six,2))), float("{0:.2f}".format(round(nine,2)))]
    tan += [float("{0:.2f}".format(round(thirty,2))),float("{0:.2f}".format(round(six,2))), float("{0:.2f}".format(round(nine,2)))]

    print(f"Sin series {sin}")
    print(f"Cos series {cos}")
    print(f"tan series {tan}")

fourth()


def fifth():
    print("Enter number of integers")
    n = int(input())
    print("Enter values")
    l = []
    for i in range(n):
        x = int(input())
        l.append(x)

    print(f"List of integers {l}")
    l.sort()
    if(n%2!=0):
        print(f"Median of list {l} == {l[n//2]}")
    else:
        print(f"Median of list {l} == {(l[n//2] + l[n//2-1])/2}")

def sixth():
    print("Enter number of integers")
    n = int(input())
    print("Enter values")
    l = []
    for i in range(n):
        x = int(input())
        l.append(x)

    print(f"List of integers {l}")
    print(f"Maximum is {max(l)}")
    print(f"Minimum is {min(l)}")

def seven():
    x = input("Enter a string")
    f = set()
    for i in x:
       f.add(i)

    for i in f:
        print(f'{i} occurs {x.count(i)} times')


def eight():
    amount = float(input("Enter the investment amount : "))
    time = int(input("Enter number of years : "))
    rate = float(input("Enter number of years"))
    interest = (amount * rate)/100
    for i in range(1,time+1):
        bal = amount + interest
        print("%40d %30.2f %20.2f %10.2f " %(i,amount,interest,bal))
        amount = bal
        interest = (amount*rate)/100





