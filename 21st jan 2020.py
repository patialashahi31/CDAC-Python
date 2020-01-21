def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i

    return fact

def oddEven():
    num = int(input())
    if(num%2==0):
        print("even")
    else:
        print("odd")

def grades(*marks):
    sum = 0
    for i in range(len(marks)):
        sum = sum + marks[i]

    avg = sum/(len(marks)*100)
    print(len(marks))
    if(avg>=90):
        print("Grade A")
    elif(avg>=80 and avg<=89):
        print("Grade B")
    elif(avg>=70 and avg<=79):
        print("Grade C")
    elif(avg>=60 and avg<=69):
        print("Grade D")
    else:
        print("Grade E")

#grades(10,20)

#large = lambda x=int(input("Enter first")),y=int(input("Enter second")):x if x>y else y
#print(large())

#cube = lambda x=int(input("Enter a number")):x**3
#print(cube())

#raisefour =  lambda x=int(input("Enter a number")):x**4
#print(raisefour())

import math
#squareroot = lambda x=int(input("Enter a number")):math.sqrt(x)
#print(squareroot())

listofNumbers = [1,9,3,6,12,35,7]
divisibleBySeven = list(filter(lambda x:x%7==0,listofNumbers))
#print(divisibleBySeven)

listofstrings = ['abba','abc','hannah']
palindromes = list(filter(lambda x:x[::-1]==x[:],listofstrings))
print(palindromes)
