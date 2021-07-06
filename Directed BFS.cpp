/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include<bits/stdc++.h>
using namespace std;
class Solution{
    public:
     vector<int> Graph(int V,vector<int>adj[]){
         vector<int>bfs;
         vector<int>vis(V+1,0);
         for(int i=1;i<=V;i++){
             if(!vis[i]){
                 queue<int>q;
                 q.push(i);
                 vis[i]=1;
                 while(!q.empty()){
                     int node=q.front();
                     q.pop();
                     bfs.push_back(node);
                     for(auto it:adj[node]){
                         if(!vis[it]){
                             q.push(it);
                             vis[it]=1;
                         }
                     }
                 }
             }
         }
         return bfs;
     }
};
   
int main()
{
    int v;
    cin>>v;
    int n;
    cin>>n;
    vector<int>k[v+1];
    for(int i=1;i<=n;i++){
        int g,h;
        cin>>g>>h;
        k[g].push_back(h);
    
        
    }
    
   // cout<<v[0];
    
    Solution s;
vector<int> e=s.Graph(v,k);
vector<int>::iterator it;
for(auto x:e){
    cout<<x<<" ";
}

    return 0;
}
