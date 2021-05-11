#include <iostream>
#include <cmath>
using namespace std;
bool isprime(long int b){
    long int i;
    if(b<=1)return 0;
    for(i=2;i<=sqrt(b);i++){
        if(b%i==0)return 0;
        
    }
    return 1;
}

int main() {
   
    long long int a;
    cin>>a;
    while(a--){
        long int b;
        cin>>b;
        if(isprime(b))cout<<"yes\n";
        else cout<<"no\n";
      
      
    }
    return 0;
}
