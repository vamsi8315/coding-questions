/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
typedef long long int ll;
using namespace std;
bool** partition(ll a[],ll sum,ll n){
 bool part[n+1][sum+1];
 for(ll i=0;i<sum+1;i++){
     part[0][i]=false;
     
 }
 
 for(ll i=0;i<n+1;i++){
     part[i][0]=true;
     
 }
  for(int i=0;i<n;i++)cout<<a[i]<<endl;
 for(ll  i=0;i<n+1;i++){
     for(int j=0;j<sum+1;j++){
         cout<<part[i][j]<<" ";
     }
     cout<<"\n";
 }
 
 for(ll i=1;i<n+1;i++){
     for(ll j=1;j<sum+1;j++){
        part[i][j]=part[i-1][j];
        if(j>=a[i-1]){
            part[i][j]=part[i][j] or part[i-1][j-a[i-1]];
        }
     }
     
 }
 for(int i=0;i<n;i++)cout<<a[i]<<endl;
 for(ll  i=0;i<n;i++){
     for(int j=0;j<sum+1;j++){
         cout<<part[i][j]<<" ";
     }
     cout<<"\n";
 }}
int main()
{
    ll n;
    cin>>n;
    ll a[n],sum=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum=sum+a[i];
        
    }
    sum=ll(sum/2);
     partition(a,sum,n);

    return 0;
}
