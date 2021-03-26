l=int(input())
e=0
for i in range((l)):
    
    s=int(input())
    k=list(map(int,input().split()))
    aa=k[::]
    arr=[]
    e=e+1
    for i in range(len(k)):
        if i==len(k)-1:
            break
        q=[]
        j=aa.index(min(aa[i:]))
        arr.append(j-i+1)
        w=[]
        for s in range(i,j+1):
            w.append(aa[s])
        w.reverse()
        #print(w)
        q=aa[0:i]+w+aa[j+1:]
        aa=q
       # print(q)
      #  ka=aa[0:i]aa[i:j+1].reverse()+aa[j+1:]
    
    print("Case #"+str(e)+":"+" "+str(sum(arr)))
    
        
        
