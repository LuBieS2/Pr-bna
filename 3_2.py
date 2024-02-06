def modulotwojstary(a, x, M):
    if x==0:
        return 1
    if x%2==0:
        w = modulotwojstary(a, x / 2, M)
        return w*w % M
    if x%2==1:
        w = modulotwojstary(a, (x - 1) / 2, M)
        return a*w*w % M
print(modulotwojstary(2, 4, 11))
#TO JEST POPIERDOLONE KURWA
