l=list(input())
k=int(input())
h=l
for i in range(k):
    sa=''
    s=input()
    a=0
    for i in range(len(l)):
            if(a<len(s)):
                if(s[a]==l[i]):
                    sa=sa+s[a]
                    a=a+1    
    if(sa==s):
        print("POSITIVE")
    else:
        print("NEGATIVE")
