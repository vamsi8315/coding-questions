import time
f=[0]*100
f[0]=0
f[1]=1
for i in range(2,100):
    f[i]=f[i-1]+f[i-2]
print(f)
print(time.process_time())
             
