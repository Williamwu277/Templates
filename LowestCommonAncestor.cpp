#include <bits/stdc++.h>
using namespace std;
#define int long long

const int MLOG = 13, MAXN = 6000;
int N, Q;
vector<pair<int, int>> adj[6005];

struct blift_lca{
    int arr[MAXN+5][MLOG+1], depth[MAXN+5], dist[MAXN+5];
    void dfs(int cur, int par){
        for(pair<int, int> nxt: adj[cur]){
            if(nxt.first != par){
                arr[nxt.first][0] = cur;
                depth[nxt.first] = depth[cur]+1;
                dist[nxt.first] = dist[cur] + nxt.second;
                for(int i=1; i<=MLOG; i++){
                    arr[nxt.first][i] = arr[ arr[nxt.first][i-1] ][i-1];
                }
                dfs(nxt.first, cur);
            }
        }
    }
    void init(){
        for(int i=0; i<=MLOG; i++){
            arr[1][i] = 1;
        }
        dfs(1, 1);
    }
    int find_lca(int x, int y){
        if(depth[x] < depth[y]) swap(x, y);
        int k_up = depth[x] - depth[y];
        for(int i=0; i<=MLOG; i++){
            if(k_up & (1 << i)){
                x = arr[x][i];
            }
        }
        if(x == y) return x;
        for(int i=MLOG; i>=0; i--){
            if(arr[x][i] != arr[y][i]){
                x = arr[x][i];
                y = arr[y][i];
            }
        }
        return arr[x][0];
    }
    int query(int x, int y){
        int lca = find_lca(x, y);
        return dist[x] + dist[y] - 2 * dist[lca];
    }
};

blift_lca thonk;

signed main(){
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> N;
    for(int i=1; i<N; i++){
        int a, b, c; cin >> a >> b >> c; a++; b++;
        adj[a].push_back({b, c});
        adj[b].push_back({a, c});
    }
    thonk.init();
    cin >> Q;
    for(int i=1; i<=Q; i++){
        int a, b; cin >> a >> b; a++; b++;
        cout << thonk.query(a, b) << "\n";
    }
}