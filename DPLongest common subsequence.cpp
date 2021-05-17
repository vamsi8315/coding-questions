#include <iostream>
typedef long long int ll;
using namespace std;

int main()
{
    string s1,s2;
    cin>>s1>>s2;
    ll m,n;
    m=s1.length()+1;
    n=s2.length()+1;
    ll a[m][n];
    for(int i=0;i<m;i++){
        a[i][0]=0;
    }
    for(int j=0;j<n;j++){
        a[0][j]=0;
        
    }
    for(int i=1;i<m;i++){
        for(int j=1;j<n;j++){
            if(s1[i-1]==s2[j-1]){
                a[i][j]=1+a[i-1][j-1];
            }
            else{
                a[i][j]=a[i-1][j]>a[i][j-1]?a[i-1][j]:a[i][j-1];
            }
              
        }
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            cout<<a[i][j]<<" ";
        }
        cout<<"\n";
    }
    ll index=a[m-1][n-1];
    ll i=m-1,j=n-1;
    string s="";
    while(i>0 and j>0){
        if(s1[i-1]==s2[j-1]){
            s=s1[i-1]+s;
            index--;
            i--;
            j--;
            
        }
        else{
            if(a[i-1][j]>a[i][j-1])i--;
            else j--;
        }
    }
    //for(ll i=0;i<index;i++)cout<<s[i];
    cout<<s; 
    return 0;
}
//@code by M P V N VAMSI
