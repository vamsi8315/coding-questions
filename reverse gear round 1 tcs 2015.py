l=int(input())
for i in range(l):
    k=list(map(int,input().split()))
    sum1=0
    time=0
    while(sum1<k[3]):
        sum1=sum1+k[1]
        print(sum1)
        time=time+k[1]*k[2]
        if(sum1==k[3]):
            break
        elif(sum1>k[3]):
            time=time-abs(sum1-k[3])*k[2]
            break
        else:
            sum1=sum1-k[0]
            print(sum1)
            time=time+k[2]*k[0]
    print(time)
            
