#include <bits/stdc++.h>
using namespace std;

long long arr[100005];

struct segtree{

    struct node{
        int left, right; long long val;
    };

    node seg[400005];

    void build(int cur, int left, int right){
        if(left == right) seg[cur] = {left, right, arr[left]};
        else{
            int mid = (left + right) / 2;
            build(cur*2, left, mid);
            build(cur*2+1, mid+1, right);
            seg[cur] = {left, right, seg[cur*2].val + seg[cur*2+1].val};
        }
    }

    void update(int cur, int ind, long long val){
        if(seg[cur].left == ind && seg[cur].right == ind){
            seg[cur].val = val;
        }else{
            int mid = (seg[cur].left + seg[cur].right) / 2;
            if(ind <= mid){
                update(cur*2, ind, val);
            }else{
                update(cur*2+1, ind, val);
            }
            seg[cur].val = seg[cur*2].val + seg[cur*2+1].val;
        }
    }

    long long query(int cur, int left, int right){
        if(left > seg[cur].right || right < seg[cur].left) return 0;
        else if(left <= seg[cur].left && seg[cur].right <= right) return seg[cur].val;
        return query(cur*2, left, right) + query(cur*2+1, left, right);
    }
};

int main() {
    return 0;
}