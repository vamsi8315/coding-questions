l=int(input())
for i in range(l):
    k=list(map(int,input().split()))
    s=[0]*k[0]
   # k[1]=k[1]-1
    x=0
    for i in range(0,k[0]):
        for i in range(i,k[0]):
            if(k[0] and k[1]):
                s[i]=s[i]+1
                k[1]=k[1]-1
   # print(k[1])
               
            

           
          #  print(k[1])
    s[0]=k[1]+1
    print(*s)
        




