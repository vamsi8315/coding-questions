arr=[[0 for i in range(6)]for i in range(6)]
row=6
col=6
counter=1
for i in range(col):#upper matrix
  if(i==0):
    arr[row-1][i]=counter
    print(arr)
    counter =counter +1
  else:
    r1=row-1
    r2=i
    for j in range((i+1)):
      arr[r1][r2]=counter
      print(r1,r2,counter)
      r2=r2-1
      r1=r1-1
      counter=counter+1
for i in range(len(arr)):
  print(*arr[i])    
  
x=row
y=col
for i in range(row-1):
  r1=row-2
  r2=col-1
  for j in range(x-(i+1)):
        arr[r1][r2]=counter
        counter=counter+1
        print(r1,r2)
        r2=r2-1
        r1=r1-1
      #if(r1<0 or r2<0):
       # break
  row=row-1
    
 # row=rwo
  
  
  
for i in range(len(arr)):
  print(*arr[i])
#print(arr)
