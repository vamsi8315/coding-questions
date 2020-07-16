l=int(input())
s=[[0 for i in range(l)]for i in range(l)]
   
print(s)
counter=1

for i in range(l//2):
  row=col=i
  endcol=l-i-1#end col is used to end the while loop
 #u endcol=0
  while(col<endcol):
    s[row][col]=counter#top view by considering row and column
    counter=counter+1
    col=col+1
  endrow=l-i-1
  while(row<endrow):
    s[row][col]=counter#rigtht side view 
    counter=counter+1
    row=row+1
  endcol=i
  while(col>endcol):
    s[row][col]=counter
    counter=counter+1#downside view 
    col=col-1
  endrow=i
  while(row>endrow):
    s[row][col]= counter#left side view
    counter=counter+1
    row=row-1
if(l%2==0):
  pass
else:
  s[l//2
  ][l//2]=l*l
  
  
for i in range(len(s)):
  for j in range(len(s[i])):#it is used to print the matrix but its not fullfilled
    print(s[i][j],end="  ")
  print()
  
