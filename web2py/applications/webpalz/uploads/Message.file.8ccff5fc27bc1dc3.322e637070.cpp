/*************************************************************





You are given an unweighted, undirected graph. Write a program to check if it's a tree topology.
Input

The first line of the input file contains two integers N and M --- number of nodes and number of edges in the graph (0 < N <= 10000, 0 <= M <= 20000). Next M lines contain M edges of that graph --- Each line contains a pair (u, v) means there is an edge between node u and node v (1 <= u,v <= N).
Output

Print YES if the given graph is a tree, otherwise print NO.
Example

Input:
3 2
1 2
2 3

Output:
YES





**************************************************************/


#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<int,int> Links;
    int n,m,N1,N2;
    int flag=0;

    cin>>n>>m;
    if(m!=n-1) 
    {
        flag=1;
    }

  
    while(m!=0)
    {
        m--;
        cin>>N1>>N2;

        if(Links[N1] && Links[N2]) 
        {
            flag=1;
            
        }
       Links[N1]=1;
       Links[N2]=1;
    }

  if(flag==1)
   cout<<"NO"<<endl;

   else
    cout<<"YES"<<endl;

    return 0;
}


