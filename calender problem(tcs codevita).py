l=int(input())
days= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'kryptonday', 'coluday', 'daxamday']
#print(days)
for i in range(l):
    k=int(input())
    if(k<296):
        d=k%10
        print(days[d])
    elif(k>=296):
        while(k>=296):
            k=k-296
        d=k%10
        print(days[d])




