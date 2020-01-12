
def  first():
    x = input("Enter a string")
    y = x[::-1]

    if(x==y):
        print("String is palindrome")
    else:
        print("String is not palindrome")


def second():
    x = input("Enter a string")
    list = [',','*','#','@','!','%','&','(',')','+','-','$']
    for i in list:
        x = x.replace(i,"")

    print("New string is " + str(x))

def third():
    a = input("Enter first string")
    b = input("Enter second string")
    y=""
    i=0
    while(i<max(len(a),len(b))):
        y = y+a[i]
        y = y+b[i]
        i=i+1

    print(y)

def fourth():
    a = input("Enter a string")
    b = input("Enter a separator")
    c = int(input("Enter count "))
    d = []
    for i in range(0,c):
        d.append(a)
    b = b.join(d)


    print(b)


def fifth():
    a = input("Enter a string")
    if(len(a)%2==0):
        print(a[0:len(a)//2])
    else:
        print("Null")




import json, urllib.request
def sixth():
    url = 'http://python-data.dr-chuck.net/comments_42.json'
    json_url = urllib.request.urlopen(url)
    data = json.loads(json_url.read())
    comment = data['comments']
    print("Count = " + str(len(comment)))
    sum=0
    for i in range(0,len(comment)):
        sum = sum + comment[i]['count']

    print(sum)

def seven():
    strg = 'dGhpcyBpcyBObyBjaGVjayBmb3lgZW5jb2RllGFuZCBkZWNvZGUc'
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    res = ""
    for i in strg:
        if i in numbers:
            continue
        res = res + i.lower()
        res.replace('pcy',"")
    print(res)



def eight():
    vowel = ['a','e','i','o','u']
    x = input("Enter a string")
    count=0
    for i in x:
        y = i in vowel
        if(y==True):
            count=count+1


    print(f'Count of vowels = {count}')
    counta=0
    counte=0
    counti=0
    counto=0
    countu=0
    for i in x:
        if(i==vowel[0]):
            counta = counta+1
        elif(i==vowel[1]):
            counte = counte+1
        elif(i==vowel[2]):
            counti = counti + 1
        elif(i==vowel[3]):
            counto = counto + 1
        elif(i==vowel[4]):
            countu = countu + 1

    if(counta!=0):
        print(f'a occurs {counta} times')
    if(counte!=0):
        print(f'e occurs {counte} times')
    if (counti != 0):
        print(f'i occurs {counti} times')
    if (counto != 0):
        print(f'o occurs {counto} times')
    if (countu != 0):
        print(f'u occurs {countu} times')







print("1) Palindrome string")
print("2) Remove punctuations")
print("3) Print alternate characters of 2 strings one by one")
print("4) Use string , separator, count and print a string with that separator")
print("5) if length of string is odd then print half length else null")
print("6) Load json")
print("7) Decode the received string 'd'")
print("8) check how many vowels present in the  string and count of each vowel")


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
else:
    eight()






