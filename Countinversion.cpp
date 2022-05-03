/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
//#include<bits/stdc++.h>
using namespace std;
int  merge(int *arr,int low,int mid,int high){
    int inv_count=0;
    int i=low;
    int k=0;
    int j=mid+1;
    int temp[high-low+1];
    while(i<=mid and j<=high){
        if(arr[i]<=arr[j]){
            temp[k]=arr[i];
            i++;
            k++;
        }
        else{
            temp[k]=arr[j];
            j++;
            inv_count+=(mid+1-i);
            k++;
        }
        
        
    }
    while(i<=mid){
        temp[k]=arr[i];
        k++;
        i++;
    }
    while(j<=high){
        temp[k]=arr[j];
        k++;
        j++;
        
    }
    for(int i=low;i<=high;i++){
        arr[i]=temp[i-low];
     //   cout<<arr[i]<<" ";
    }
    return inv_count;
}
int mergesort(int *arr,int low,int high){
    int mid;
    int inv=0;
    if(low<high){
        
         mid=(low+high)/2;
        inv=inv+mergesort(arr,low,mid);
        inv=inv+mergesort(arr,mid+1,high);
       // cout<<"djj";
        inv=inv+merge(arr,low,mid,high);
    }
    return inv;
}

int main()
{
    int arr[]={5,3,2,4,1};
    int low=0;
    int high=4;
   int k= mergesort(arr,low,high);
   cout<<k;
for(int i=0;i<5;i++){
    cout<<arr[i]<<" ";
}
    return 0;
}
