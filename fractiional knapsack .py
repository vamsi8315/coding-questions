k=list(map(int,input().split()))
profit=[]
weight=[]
for i in range(k[0]):
    s=list(map(int,input().split()))
    profit.append(s[0])
    weight.append(s[1])
#print(profit,weight)
w1=weight[::]

summ=0
maxval=[]
#print(weight,w1)
for i in range(len(profit)):
    maxval.append(profit[i]/weight[i])

#print(maxval)    
for i in range(len(profit)):
    sa=maxval.index(max(maxval))
    maxval[sa]=0
    #print(maxval,sa)
    if(weight[sa]<k[1]):
        k[1]=k[1]-weight[sa]
        summ=summ+profit[sa]
    elif(weight[sa]==k[1]):
        k[1]=0
        summ=summ+profit[sa]
        #print(summ,weight[sa])
        break
    else:
        summ=summ+(profit[sa]/weight[sa])*k[1]
        k[1]=0
        break
print(summ)
        
        
    
    

 
"""
# Uses python3
import sys

#The key points here are selecting max index from value/weight.
#Add that value to result and clean that value in original list.

def get_optimal_value(capacity, weights, values):
    value = 0.
    if capacity == 0:
        return 0
    for i in range(n):
        max_index = select_max_index(values, weights)
        if max_index >= 0:
            available_weights = min(capacity, weights[max_index])
            value = value + available_weights * values[max_index]/weights[max_index]
            weights[max_index] = weights[max_index] - available_weights
            capacity = capacity - available_weights

    return value

def select_max_index(values, weights):
    index = -1
    max = 0
    for i in range(n):
        if weights[i] > 0 and (values[i] / weights[i]) > max:
            max = values[i]/weights[i]
            index = i
    return index


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    print(values,weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
"""
