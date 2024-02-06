from string import ascii_uppercase, ascii_lowercase
def is_empty(array, n):
    print(" ")
    for i in range(len(array)):
        print(array[i][n])
        if array[i][n]==".":
            pass
        else:
            return False
    return True
def loaddata(data):
    data=open(data, "r")
    file=list(map(str.strip, data.readlines()))
    return  file
def chess():
    chess=loaddata("szachy_przyklad.txt")
    print(chess)
    chess2=[]
    temp=[]
    k=1
    print(len(chess))
    for n in range(len(chess)+1):
        if n!=k*9-1:
            temp.append(chess[n])
        else:
            k+=1
            chess2.append(temp)
            temp=[]
    print(chess2)
    return chess2
def zad1():
    chess2=chess()
    max=0
    c=0
    for board in chess2:
        n=0
        for i in range(8):
            is_empty(board, i)
            if is_empty(board, i)==True:
                n+=1
                if n>max:
                    max=n
                print(board)
        if n>0:
            c+=1
    print(max, c)
    for board in chess2:
        print(board)
def zad2():
    S=list(ascii_lowercase)
    s=0
    U=list(ascii_uppercase)
    u=0
    chess2=chess()
    d=0
    n=64
    for board in chess2:
        u = 0
        s = 0
        for item in board:
            for i in item:
                print(i)
                if i in S:
                    s+=1
                if i in U:
                    u+=1
                print(s, u)
        if s==u:
            if s<n:
                n=s+u
            d+=1
    print(d,n)
print(chess())
def zad3():
    C=0
    B=0
    chess2=chess()
    index=0
    for board in chess2:
        for line in board:
            for i in range(len(line)):
                if line[i]=="K":
                    for n in range(i, len(line)):
                        if line[n]!="." or line[n]!="K":
                            if line[n]=="w":
                                C+=1
                        if board[n][i]!="." or line[n]!="K":
                            if line[n]=="w":
                                C+=1
                if line[i] == "k":
                    for n in range(i, len(line)):
                        p=0
                        q=0
                        print(line[n])
                        if line[n] == "." or line[n] == "k":
                            pass
                        else:

                            p+=1
                            if line[n] == "W" and p==1:
                                print(line)
                                B += 1
                        if board[n][i] == "." or board[n][i] == "k":
                            pass
                        else:
                            q += 1
                            if board[n][i] == "W" and q == 1:
                                    print(board[n][i])
                                    B += 1
    print(C, B)
zad3()