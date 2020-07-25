l=int(input())
kas=1
for i in range(l):
    le=int(input())
    I=list(input())
    O=list(input())
    mat=[[0 for i in range(le)]for i in range(le)]
   # print(mat,I,O)
    for i in range(le):
        for j in range(le):
            if(abs(i-j)==1):
                if(O[i]=='Y'):
                    if(I[j]=="Y"):
                        mat[i][j]="Y"
                    else:
                        mat[i][j]="N"
                else:
                    mat[i][j]="N"

            
            elif(i==j):
                mat[i][j]="Y"
            else:
                mat[i][j]="N"
            lal=0
            for s in range(min(i,j)+1,max(i,j)):
                if(O[i]=="Y"):
                    if(I[j]=="Y"):
                        if(I[s]=="Y" and O[s]=="Y"):
                            lal=lal+1
            #print(lal)
            if(lal>0 and lal==abs(i-j)-1):
                mat[i][j]="Y"
                            
    print("Case "+"#"+str(kas)+":")
    kas=kas+1
    for i in range(le):
         print(*mat[i],sep="")
    

        
                        
    
