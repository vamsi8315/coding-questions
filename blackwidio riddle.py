l=int(input())
for i in range(l):
    k=list(map(int,input().split()))
  #  print(k)
    row=k[0]
    col=k[1]
    k.remove(k[0])
    k.remove(k[0])
    arr=[[0 for x in range(col)]for x in range(row)]
  #  print(arr[0][0])
    for i in range(len(arr)):
        s=[]
        for j in range(len(arr[i])):
       #     print(i,j)
            arr[i][j]=k[j]
        #    print(arr)
        #    print(k[j])
            s.append(k[j])
       # print(k,arr)
        for i in range(len(s)):
            k.remove(s[i])
  #      print(k)
    
   # print(arr)
    rowt=0
    for i in range(len(arr)):
        if(len(set(arr[i]))==len(arr[i])):
            pass
        else:
            rowt=rowt+1
   # print(rowt)
    x=[]
    ra=0
    for i in range(len(arr)):
        la=[]
        
        for j in range(len(arr)):
            la.append(arr[j][i])
        if(len(set(la))==len(la)):
            pass
        else:
            ra=ra+1
   # print(ra)
    if(rowt ==0 and ra ==0):
        print("SAFE")
    else:
        print("DANGER",rowt,ra)
           
   
    #for i in range(len())
            
