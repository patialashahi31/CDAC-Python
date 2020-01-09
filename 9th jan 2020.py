from math import sin,cos,tan,radians,sqrt,pow,pi
import random as rd
def first():
    #sin , cos , tan values
    zero = radians(0)
    thirty = radians(30)
    fortyfive = radians(45)
    sixty = radians(60)
    ninety = radians(90)
    oneeighty = radians(180)
    print('       0                   30                  45                   60                   90                   180')
    print(f'sin    {sin(zero)}       {sin(thirty)}       {sin(fortyfive)}       {sin(sixty)}       {sin(ninety)}       {sin(oneeighty)}')
    print(f'cos    {cos(zero)}       {cos(thirty)}       {cos(fortyfive)}       {cos(sixty)}       {cos(ninety)}       {cos(oneeighty)}')
    print(f'tan    {tan(zero)}       {tan(thirty)}       {tan(fortyfive)}       {tan(sixty)}       {tan(ninety)}       {tan(oneeighty)}')



def second():
    #distance between 2 points
    print("Enter coordinates of first point")
    x1 = int(input("Enter x-coordinate"))
    y1 = int(input("Enter y-coordinate"))
    print("Enter coordinates of second point")
    x2 = int(input("Enter x-coordinate"))
    y2 = int(input("Enter y-coordinate"))
    distance = sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    print(f'Distance between A({x1},{y1}) and B({x2},{y2}) points is {distance}')

def third():
    for i in range(0,10):
        print(rd.randrange(1,100))



def fourth():
    radius = int(input("Enter radius of a circle"))
    area = pi*radius*radius
    print(f'Area of circle with {radius} is {area}')


print("1) sin , cos and tan values")
print("2) Distance between 2 numbers")
print("3) Generate 10 random numbers between 1 to 100")
print("4) Area of a circle")

choice = int(input("Enter your choice"))

if choice==1:
    first()
elif choice==2:
    second()
elif choice==3:
    third()
else:
    fourth()

