a=int(input())
b=[[0 for x in range(a)]for x in range(a)]
for i in range(1,a+1):
    for j in range(1,a+1):
        m=max(i,j)
        f=m*(m-1)+1+((-1)**m)*(i-j)
        b[i-1][j-i]=f
for o in range(len(b)):
    t=(b[o][-o:] + b[o][:-o])
    print(*t)
