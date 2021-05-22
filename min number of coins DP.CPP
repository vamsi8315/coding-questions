/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
//#include<bits/std.c++.h>
typedef long long int ll;
#define inf 10000000000;


using namespace std;

int main()
{
    ll a;
    cin>>a;
    ll arr[a];
    for(ll i=0;i<a;i++){
        cin>>arr[i];
        
    }
ll amt;
cin>>amt;
ll dp[a+1][amt+1];
for(ll i=0;i<amt+1;i++){
    dp[0][i]=inf;}
for(ll i=0;i<a+1;i++){
    dp[i][0]=0;
}
for(ll  i=1;i<a+1;i++){
    for(ll j=1;j<amt+1;j++){
        ll ainc=1+dp[i][j-arr[i-1]];
        ll dec=dp[i-1][j];
        dp[i][j]=ainc>dec?dec:ainc;
    }
}
for(ll i=0;i<a+1;i++){
    for(ll j=0;j<amt+1;j++){
        cout<<dp[i][j]<<" ";//for printing the array
    }
cout<<"\n";
    
}
cout<<"the minimum number of coins is "<<dp[a][amt];
    return 0;
}
