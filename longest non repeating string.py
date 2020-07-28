from itertools import combinations
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f=[]
        res=[s[x:y] for x,y in combinations(range(len(s)+1),r=2)]
        #print(s)
        var=0
        for i in range(len(res)):
                x=list(res[i])
                if(len(set(x))==len(x)):
                    if(var<len(x)):
                        var=len(x)
                        print(var)
        if(var==0):
            return("0")
        else:
            return(var)
        
