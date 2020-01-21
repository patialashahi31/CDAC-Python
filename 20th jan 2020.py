
#Create nested dictionary, add and delete elements
def first():
    school = {1:{'name':'Yo','Age':22},2:{'name':'Hi','Age':26}}
    print(school)
    print("Adding elements")
    school[3] = {'name':'Hello'}
    print(school)



    print("Removing elements")
    del school[3]
    print(school)

import numpy as np
def second():
    a = np.array([[1,2],[4,5]])
    b = np.array([[7,8],[10,11]])
    print(f'a*b = {a*b}')
    print(f'a.dot(b) = {np.dot(a,b)}')


def third():
    n1 = int(input("Enter rows"))
    a = []
    for i in range(n1):
        row = input().split()
        print(row)
        for i in range(len(row)):
            row[i] = int(row[i])
        a.append(row)
    print(a)

    b = []
    for i in range(n1):
        row = input().split()
        print(row)
        for i in range(len(row)):
            row[i] = int(row[i])
        b.append(row)
    print(b)
    a = np.array(a)
    b = np.array(b)
    print(f'a+b :: {a+b}')
    print(f'a*b = {a * b}')


