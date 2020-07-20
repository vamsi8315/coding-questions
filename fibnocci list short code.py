import time
f=[0]*100
f[0]=0
f[1]=1
for i in range(2,100):
    f[i]=f[i-1]+f[i-2]
print(f)
print(time.process_time())
             
#next version of the code below
import time
def fib(n):
    f=[0]*n
    f[0]=0
    f[1]=1
    if(n>1):
        for i in range(2,n):
            f[i]=f[i-1]+f[i-2]
        return(f)
    return(f)
l=int(input())
if(l==0):
    print("0")
elif(l==1):
    print("1")
else:
    x=fib(l+1)
    print(x[l])


