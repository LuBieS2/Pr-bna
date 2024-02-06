from zadanie1 import loaddata
def mod(M, a, b):
    for x in range(y):
        if (a**x) % M == b:
            return True
    return False
def dividers(a):
    d=[]
    for i in range(int(a+1)):
        if i==0:
            pass
        elif a%i==0:
            d.append(i)
    return d
def isprime(number):
    if number==1 or number==0:
        return False
    for i in range(int(number**(1/2))+1):

        if i==1 or i==0:
            pass
        elif number%i==0:
            return False
    return True
def zad1():
    numbers=loaddata("liczby.txt")
    numbers=[item.split(" ") for item in numbers]
    print(numbers)
    M=[]
    for i in numbers:
        M.append(int(i[0]))
    c=0
    for i in M:
        if isprime(i):
            c+=1
    print(c)

def zad2():
    numbers=loaddata("liczby.txt")
    numbers=[item.split(" ") for item in numbers]
    l=0
    m=[]
    for i in numbers:
        c = 0
        M=dividers(int(i[0]))
        a=dividers(int(i[1]))
        for i in M:
            if i!=1 and i in a:
                c+=1
        if c==0:
            l+=1
            m.append([M, a])
    print(l)
def zad3():
    numbers=loaddata("liczby.txt")
    numbers=[item.split(" ") for item in numbers]
    c=0
    for i in numbers:
        print(i)
        if mod(int(i[0]),int(i[1]),int(i[2])):
            c+=1
    print(c)
zad3()
