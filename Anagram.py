//Anagram ........
s1=(input())
s2=(input())
charcount=[]
for i in range(26):
    charcount.append(0)
for i in range(len(s1)):
    charcount[ord(s1[i])-ord('a')]+=1
for i in range(len(s2)):
    charcount[ord(s2[i])-ord('a')]-=1
aa=0
for i in range(len(charcount)):
    if(charcount!=0):
        aa=aa+abs(charcount[i])
print(aa)
    
        
