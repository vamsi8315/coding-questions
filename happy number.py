#isHappyNumber() will determine whether a number is happy or not    
import time
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
req=[]       
first=int(input())
last=int(input())
for i in range(first,last+1):
    number=i
    result=number
    while(result != 1 and result != 4):
        result = isHappyNumber(result)
    
    if(result == 1):
         req.append(number)  
print(req)
requ=int(input())
print(time.process_time())
