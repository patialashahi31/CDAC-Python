#Searching in a list
def first():
    print("Enter 15 marks")
    marks = []
    for i in range(15):
        x = int(input("Enter value"))
        marks.append(x)

    find = []
    query = int(input("Enter a number you want to find"))
    for i in range(15):
        if(query==marks[i]):
            find.append(i)

    if(len(find)==0):
        print(f'There is no {query} in list {marks}')
    else:
        print(f'{query} is found at indexes {find[:]}')

#Sum of diagonal elements
def second():
    n = int(input("Enter rows"))
    a = []
    for i in range(n):
        row = input().split()
        print(row)
        for i in range(len(row)):
            row[i] = int(row[i])
        a.append(row)
    print(a)


    sum = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(i==j):
                sum = sum + a[i][j]

    print(f'Sum of diagonal elements {sum}')

#Sum of 2 matrices
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


    c = []
    for i in range(n1):
        row = []
        for j in range(len(a[0])):
            row = row + [0]
        c.append(row)

    x = len(a[0])
    for i in range(n1):
        for j in range(x):
            c[i][j] = int(a[i][j] + b[i][j])
    print(c)


#Transpose of a matrix
def fourth():
    n1 = int(input("Enter rows"))
    a = []
    for i in range(n1):
        row = input().split()
        print(row)
        for i in range(len(row)):
            row[i] = int(row[i])
        a.append(row)
    print(a)


    for i in range(n1):
        for j in range(len(a[0])):
            a[i][j] = a[j][i]

    print(a)

def fifth():
    n1 = int(input("Enter rows"))
    a = []
    for i in range(n1):
        row = input().split()
        print(row)
        for i in range(len(row)):
            row[i] = int(row[i])
        a.append(row)
    print(a)

    n2 = int(input("Enter rows"))
    b = []
    for i in range(n1):
        row = input().split()
        print(row)
        for i in range(len(row)):
            row[i] = int(row[i])
        b.append(row)
    print(b)
    x = len(b[0])
    c=[]
    for i in range(n1):
        row = []
        for j in range(x):
            row = row + [0]
        c.append(row)


    for i in range(n1):
        for j in range(x):
            for k in range(n2):
                c[i][j] = c[i][j] + (a[i][k] * b[k][j])

    print(c)









