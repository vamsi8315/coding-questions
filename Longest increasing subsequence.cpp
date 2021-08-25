/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
// order of n^2 longest increasing sub sequence
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int omax=0;
    int dp[n];
    dp[0]=1;
    for(int i=0;i<n;i++){
        int max=0;
        for(int j=0;j<i;j++){
            if(a[j]<a[i]){
                if(dp[j]>max){
                    max=dp[j];
                }
            }
            dp[i]=max+1;
            if(dp[i]>omax){
                omax=dp[i];
            }
        }
    }
    
cout<<omax;
    return 0;
}
