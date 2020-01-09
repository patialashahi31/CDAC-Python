#Please remove triple quotes to run each program
# 1)Sum of 2 numbers
"""firstNumber = int(input("Enter first number"))
secondNumber = int(input("Enter second number"))
sum = firstNumber + secondNumber
print(sum)"""



# 2)Implicit and explicit conversion
"""num1 = 7
num2 = 7.8
num3 = num1 + num2
print("Implicit conversion as integer converts to float after addition")

num4 = "7"
print("Type before conversion" + type(num4))
num4 = int(num4)
print("After conversion" + type(num4))"""



# 3)Usage of functions type() , isinstance() , ord() , chr() , float() , str()
"""a = "hi"
print("Type of variable a" + str(type(a)))
b = "hello"
print("Check if this is string" + str(isinstance(b,str)))
print("ASCII value of A is " + str(ord('A')))
print("What 100 represents " + chr(100))
a = 10
print("I can convert to float" + str(float(10)))
print("Type of a variable" + str(type(a)))
a = str(a)
print("Type of a variable after conversion "+ str(type(a)))"""

# 4)Hello to all print in different variations
"""print("Hello to all")
print("\'Hello to all\'")
print('\"Hello to all\"')
print("\\Hello to all\\")"""


# 5) Literals
"""print(str(0xA) + " Hexadecimal literal" )
print(str(0b110) + " Binary")
print(str(0O56) +" octal")
a = True
b = False
print(f'{a} and {b} are boolean literals')
print("values {} {}".format(a,b))
c = 10 + 4j
print("Real part" + str(c.real))
print("Imaginary part " + str(c.imag))"""
