


# 1) Odd and even check
def first():
    num = int(input("Enter a number"))
    if(num%2==0):
        print("Even")
    else:
        print("Odd")


#2) Find sum and avg of numbers 1 to n and divisible by 7
def second():
    num = int(input("Enter a number"))
    sum = 0
    for i in range(1,num +1):
        if i%7==0:
            sum = sum + i

    print(f"Sum of {num} numbers = " + str(sum))
    print(f'Average of {sum} numbers = ' + str(sum/num))


#3) Find sum of first n numbers
def third():
    num = int(input("Enter a number"))
    sum = 0
    for i in range(1,num+1):
        sum = sum + i

    print(f"Sum of 1 to {num} numbers = " + str(sum))


#4) Factorial of a number
def fourth():
    num = int(input("Enter a number"))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i

    print(f"Factorial of {num} = " +str(fact))

#5) Find greatest of 3 numbers
def fifth():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter first number"))
    num3 = int(input("Enter first number"))
    if(num1>=num2 and num1>=num3):
        print(f'{num1} + is greatest from {num1} , {num2} , {num3}')
    elif(num2>=num1 and num2>=num3):
        print(f'{num2} + is greatest from {num1} , {num2} , {num3}')
    else:
        print(f'{num3} + is greatest from {num1} , {num2} , {num3}')

#6) 128 Ascii characters and
def sixth():
    for i in range(1,129):
        x = chr(i)
        print(f'{x} represents ' + str(ord(x) ))

#7) Input name and print ascii values of characters
def seven():
    name = input("Enter your name")
    for i in name:
        print(f'{i} represents ' + str(ord(i)))

#8) Print sum of series 1**2 + 4**2 +.... n
def eight():
    num = int(input("Enter a number"))
    sum = 0
    for i in range(1,num+1,3):
        f = i**2
        sum = sum +f

    print(f'Sum is = {sum}')

#9) Display pattern
def nine():
    num = int(input("Enter rows"))
    for i in range(0,num):
        for j in range(0,num):
            if(j<=i):
                print("*",end="")
        print()



print("1) Odd even check")
print("2) Find sum and avg of numbers 1 to n and divisible by 7")
print("3) Find sum of first n numbers")
print("4) Factorial of a number")
print("5) Find greatest of 3 numbers")
print("6) 128 Ascii characters and codes")
print("7) Input name and print ascii values of characters")
print("8) Print sum of series 1**2 + 4**2 +.... n")
print("9) Display pattern")
choice = int(input("Enter your choice"))

if choice==1:
    first()
elif choice==2:
    second()
elif choice==3:
    third()
elif choice==4:
    fourth()
elif choice==5:
    fifth()
elif choice==6:
    sixth()
elif choice==7:
    seven()
elif choice==8:
    eight()
else:
    nine()