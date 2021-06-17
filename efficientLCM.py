def getSmallestDivNum(self, n):
        a=list(range(1,n+1))
        res=1
        for i in a:
            res=int((res*i)/math.gcd(res,i))
        return res
