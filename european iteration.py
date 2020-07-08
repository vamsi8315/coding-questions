n=int(input())

def roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
lm=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#print(lm)
while n in range(1,3999):
    summ=0
    x=str(roman(n))
    b={"I":18,"V":31,"X":33,"L":21,"C":12,"D":13,"M":22}
    max=0
    for i in x:
        if(b[i] >max):#calculating the base value of highest roman number
            max=b[i]
   # print(max)
    x=x[::-1]
    if(len(x)==1):
        n=lm.index(x)
    else:
        for i in range(len(x)):
           # print(lm.index(x[i]))
            summ=summ+((max+1)**i)*lm.index(x[i])
        n=summ
print(n)
            
    
    
    




