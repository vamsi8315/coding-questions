/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include<bits/stdc++.h>
using namespace std;
class Sollution{
    void dfs(int node,vector<int>&vis,vector<int>adj[],vector<int>&store_dfs){
        store_dfs.push_back(node);
        vis[node]=1;
        for(auto it:adj[node]){
            if(!vis[it]) {dfs(it,vis,adj,store_dfs);
            }
        }
        
    }
public:
    vector<int> dfsGraph(int V,vector<int>adj[]){
        vector<int>store_dfs;
        //store_dfs.push_back(node);
        vector<int>vis(V+1,0);
        for(int i=1;i<=V;i++){
            if(!vis[i]) dfs(i,vis,adj,store_dfs);
        }
    
        return store_dfs;
    }
};
int main()
{
    int V;
    cin>>V;
   // vector<int>vis(V+1,0);
    vector<int>adj[V+1];
    int n;//number of connections have to enter 
    cin>>n;
    for(int i=1;i<=n;i++){
        int k,v;
        cin>>k>>v;
        adj[k].push_back(v);
        adj[v].push_back(k);
    }
    Sollution s;
    vector<int>t=s.dfsGraph(V,adj);
    vector<int>::iterator a;
    for(a=t.begin();a<t.end();a++){
        cout<<*a<<" ";
    }
    return 0;
}
