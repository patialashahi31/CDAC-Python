#WAP to print 1234 as one two three four
x = input("Enter any number")
numbers = ("zero","one","two","three","four","five","six","seven","eight","nine")
res = ""
for i in range(len(x)):
        res = res + " " + numbers[int(x[i])]

print(res)



