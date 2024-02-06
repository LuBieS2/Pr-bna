A=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
#k=1
'''for i in range(20):
    A.append(k*5)
    k+=1'''
print(A)
s=200
B=[]
for i in range(s):
    if i==0:
        B.append(1)
    B.append(0)
def tura(k):
    for i in reversed(range(A[k-1], s+1)):
        print(i)
        if B[i-A[k-1]]==1 and B[i]==0:
            B[i]=1
            print(B)
for m in range(len(A)):
    tura(m)
print(B)
c=0
if B[len(B)-1]==1:
    print("Tak")