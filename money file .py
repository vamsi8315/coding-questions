l=int(input())
m=[1,2,5,10,20,50,100,500,1000]
for i in range(l):
    n=int(input())
    x=0
    
    while(n>0):
        s=0
        sa=0
        if(n in m):
            x=x+1
            n=0
        else:
            if(n>1000):
                sa=n//1000
                x=x+sa
                n=n-sa*1000
            for i in range(len(m)):
                if(m[i]>n):
                    s=m[i-1]
                    break
          #  print(s)
            
            sa=n//s
         #   print(sa)
            n=n-sa*s
            x=x+sa
         #   print(x)
    print(x)
                


