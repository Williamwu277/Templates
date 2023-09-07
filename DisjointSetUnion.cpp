#include <bits/stdc++.h>
using namespace std;

/*
disjoint set union template with compression & union by rank
O(N log N) complexity
SIZE is the number of nodes
Make sure to create it globally
disjoint_set<SIZE> tree;
run tree.init() to initialize the set
fnd(NODE_A) returns the leader of NODE_A
connected(NODE_A, NODE_B) returns if the two nodes are connected
merge(NODE_A, NODE_B) creates a path between those two nodes
*/

/* 
tested on:
> https://dmoj.ca/problem/dmpg17s2
https://dmoj.ca/submission/3884926
> https://dmoj.ca/problem/dmopc18c6p3
https://dmoj.ca/submission/3884938
> https://dmoj.ca/problem/aac3p5
https://dmoj.ca/submission/3884956
*/

template<const int MAXN> struct disjoint_set{
    int leader[MAXN], rank[MAXN];
    void init(){
        for(int i=1; i<MAXN; i++){
            rank[i] = 1; leader[i] = i;
        }
    }
    int fnd(int a){
        if(leader[a] == a) return a;
        else return leader[a] = fnd(leader[a]);
    }
    bool connected(int a, int b){
        a = fnd(a); b = fnd(b);
        return a == b;
    }
    void merge(int a, int b){
        a = fnd(a); b = fnd(b);
        if(!connected(a, b)){
            if(rank[b] > rank[a]){
                int tmp = a; a = b; b = tmp;
            }
            rank[a] += rank[b]; 
            leader[b] = leader[a];
        }
    }
};

int main(){
    return 0;
}
