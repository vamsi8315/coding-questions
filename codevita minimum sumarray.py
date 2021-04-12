q=list(map(int,input().split()))
l=list(map(int,input().split()))
k=list(map(int,input().split()))
if(min(k)<0):
   a=k.index(min(k))
   l[a]=l[a]+q[1]*2
else:
   a=k.index(max(k))
   l[a]=l[a]-q[1]*2
summ=0
for i in range(len(l)):
    summ=summ+l[i]*k[i]
print(summ)
