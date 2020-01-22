fruits = ['apple','mango','orange']
# Convert into titlecase using lambda

"""convertUsinglambda = lambda x:x.title()
new=[]
for i in fruits:
    y=convertUsinglambda(i)
    new.append(y)

print(new)

x = list(map(lambda x:x.title(),fruits))
print(x)"""

#Convert using simple function
def convert(x):
    new = []
    for i in x:
        y = i.title()
        new.append(y)

    print(new)

#convert(fruits)


temp = (36.5,37,37.5,35)
#Convert F to C
convertusinglambda = lambda x:(x-32)*(5/9)
x = list(map(convertusinglambda,temp))
#print(x)

def FtoC(temp):
    new = []
    for i in temp:
        y = (i-32)*(5/9)
        new.append(y)

    print(new)

#CtoF(temp)

#Convert F to C
convertusinglambdaCtoF = lambda x:(9/5)*x + 32
z = list(map(convertusinglambdaCtoF,temp))
#print(z)

def CtoF(temp):
    new = []
    for i in temp:
        y = 9/5*i + 32
        new.append(y)

    print(new)

#CtoF(temp)

import datetime
x = datetime.datetime.now()
print(x)
print(x.time())
