#include <stdio.h>
#include <math.h>
int checkPrime(int );
int main()
{
	int checkPrime(int n)
{
  int flag=0;
for (int i = 2; i <= sqrt(n); i++) {
 
        if (n % i == 0) {
            flag = 1;
            break;
        }
    }

    if (flag == 1) {
        return 0;
    }
    else {
        return 1;
    }

 
}
int a;
scanf("%d",&a);
int c,d;
for (int i=0;i<a;i++){
	scanf("%d %d",&c,&d);
	//printf("%d %d",c,d);
    if(c==d){
		if(checkPrime(c))
		   printf("0\n");
		else
		   printf("-1\n");}
	else{
	 int la=0,pa=0,i=0;
	    for(int j=c;j<=d;j++){
			
			if(checkPrime(j)){
				i=i+1;
				if(i==1)
				    la=j;
				else
				    pa=j;
		

			}
		}
	if(pa==0 &&la==0){
		printf("-1\n");
	}
	else if(pa==0){
		printf("0\n");

	}
	else
	printf("%d\n",(pa-la));
	}
	
	}
	
}
