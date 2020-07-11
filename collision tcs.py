l=int(input())
D={}
for i in range(l):
    s=list(map(int,input().split()))
    k=(s[0]**2+s[1]**2)/(s[2]**2)
    if(D.get(k)==None):
        D[k]=1
    else:
        D[k]=D[k]+1
c=0
for i in D:
    if(D[i]>1):
        c=c+(D[i]*(D[i]-1))/2
print(int(c))
        
