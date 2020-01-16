#input name and age and print codes
def first():
    name = input("Enter Name")
    age = int(input("Enter age"))
    x = name.split()
    code1=""
    code2=""
    for i in x:
        code1 += str(i[0].lower())

    print("Code 1: "+code1+str(age))
    for i in x:
        code2 += str(i[len(i)//2])

    print("Code 2: " + code2+str(age*2))

#input a sentence from user and output

def second():
    sentence = input("Enter sentence")
    x = sentence.split()
    maxlen = 0
    maxword =[]
    minlen = 100000
    minword = []
    for i in x:
        if(len(i)>maxlen):
            maxlen = len(i)
            maxword.append(i)

        if(len(i)<minlen):
            minlen = len(i)
            minword.append(i)

    print(f"Maximum length word is : {maxword[len(maxword)-1]}")
    print(f"Minimum length word is : {minword[len(minword)-1]}")
    vowels = ['a','e','i','o','u']
    countvowels = 0
    countconsonants =0
    for i in x:
        for j in i:
            if(j in vowels):
                countvowels = countvowels+1
            else:
                countconsonants = countconsonants+1

    print(f'Number of vowels = {countvowels}')
    print(f'Number of consonants = {countconsonants}')
    print(f'Whitespaces = {len(x)-1}')
    countdigits =0
    for i in x:
        for j in i:
            if(j.isdigit()):
                countdigits = countdigits+1

    print(f"Number of digits : {countdigits}")


#Count no. of characters in string entered by user and store in dictionary
def third():
    s = input("Enter any string")
    letters ={}
    for i in s:
        if i in letters:
            letters[i] = letters[i] + 1
        else:
            letters[i] = 1

    listofletters = list(letters.keys())
    listoffreq = list(letters.values())
    print(f"Dictionary : {letters}")
    listoffreqc = sorted(listoffreq,reverse=True)
    sortlist = sorted(letters.items(),key=lambda x:x[1],reverse=True)
    print(f"Decreasing order")
    for i in sortlist:
        print(i[0],end=" ")



def fourth():
    d = {"Ram":"15/07/1987","Krishna":"09/12/1988","Venkat":"11/02/2010"}
    date = input("Enter date in format dd-mm-yyyy")
    x = date.split('-')
    y = "/".join(x)
    c = False
    for k,v in d.items():
        if v==y:
            print("Key is found and the name is " + k)
            c = True
            break

    if(c==False):
        print("No name with this date")







