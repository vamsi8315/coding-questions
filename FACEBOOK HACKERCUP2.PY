l=int(input())
for i in range(l):
    k=int(input())
    s=list(input())
    if(s.count("A")<s.count("B")):
        x="BAB"
        neg=0
        if("B" in s):
            s.remove("B")
        else:
            neg=neg+1
        if("A" in s):
            s.remove("A")
        else:
            neg=neg+1
        if("B" in s):
            s.remove("B")
        else:
            neg=neg+1
        
        while(len(s)>1):
            if(x[len(x)-1] =="A"):
                x=x+"B"
               # s.remove("B")
                if("B" in s):
                    s.remove("B")
                else:
                    neg=neg+1
                    break
                    
            
            else:
                x=x+"A"
                if("A" in s):
                    s.remove("A")
                else:
                    neg=neg+1
                    break
                    
            
            if(len(s)==1):
                break
       # lasss=0
        if(neg==0):
            print("Case "+"#"+str(i+1)+":"+" "+"Y")
          #  lasss=lasss+1
        else:
            print("Case "+"#"+str(i+1)+":"+" "+"N")
         #   lasss=lasss+1
            
    else:
        x="ABA"
        neg=0
        if("A" in s):
            s.remove("A")
        else:
            neg=neg+1
            
        if("B" in s):
            s.remove("B")
        else:
            neg=neg+1
         #   break
        if("A" in s):
            s.remove("A")
        else:
            neg=neg+1
          #  break
        
    
        while(len(s)>1):
            if(x[len(x)-1] =="A"):
                x=x+"B"
                if("B" in s):
                    s.remove("B")
                else:
                    neg=neg+1
                    break
                    
            else:
                x=x+"A"
                if("A" in s):
                    s.remove("A")
                else:
                    neg=neg+1
                    break
            
            if(len(s)==1):
                break
        #lasss=1
        if(neg==0):
            print("Case "+"#"+str(i+1)+":"+" "+"Y")
         #   lasss=lasss+1
        else:
            print("Case "+"#"+str(i+1)+":"+" "+"N")
        #    lasss=lasss+1
            
        
                
               
            
