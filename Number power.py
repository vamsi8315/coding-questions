def power(num, n): 
  
    if(n == 0): 
        return 1
    elif(n % 2 == 0): 
        return power(num, n // 2) * power(num, n // 2) 
    else: 
        return num * power(num, n // 2) * power(num, n // 2) 
  

def check(x, n, curr_num=1, curr_sum=0): 
 
    results = 0
 
    p = power(curr_num, n) 
    while(p + curr_sum < x): 
  
        results += check(x, n, curr_num + 1, p + curr_sum) 
        curr_num = curr_num + 1
        p = power(curr_num, n) 
  
    if(p + curr_sum == x): 
        results = results + 1
  
    
    return results 
  
s = int(input())
k = int(input())
print(check(s,k)) 
