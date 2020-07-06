l=int(input())
for i in range(l):
    s=list(map(int,input().split(":")))
    h=[s[0]]
    for i in range(1,s[1]+1):
        h.append(h[i-1]*2-1)
        
        
    ha=list(map(int,str(sum(h))))
    g=""
    gt=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(ha)):
         g=g+(gt[ha[i]])
    print(g)




