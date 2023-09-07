// https://codeforces.com/contest/1616/submission/141259314

struct node{
    int left, right, val;
};
 
struct lazyseg{
    node seg[400005]; int lazy[400005];
    void prop(int cur, int val){
        seg[cur].val += (seg[cur].right - seg[cur].left + 1) * lazy[cur];
        if(seg[cur].left != seg[cur].right){
            lazy[cur*2] += val;
            lazy[cur*2+1] += val;
        }
        lazy[cur] = 0;
    }
    void build(int cur, int left, int right){
        if(left == right){
            seg[cur] = {left, right, 0}; lazy[cur] = 0;
        }else{
            int mid = (left + right)/ 2;
            build(cur*2, left, mid);
            build(cur*2+1, mid+1, right);
            seg[cur] = {left ,right, seg[cur*2].val + seg[cur*2+1].val};
            lazy[cur] = 0;
        }
    }
    void update(int cur, int left, int right, int val){
        prop(cur, lazy[cur]);
        if(left <= seg[cur].left && seg[cur].right <= right){
            seg[cur].val += (seg[cur].right - seg[cur].left + 1) * val;
            prop(cur, val);
        }else if(!(right < seg[cur].left || seg[cur].right < left)){
            update(cur*2, left, right, val);
            update(cur*2+1, left, right, val);
        }
    }
    int query(int cur, int left, int right){
        prop(cur, lazy[cur]);
        if(right < seg[cur].left || seg[cur].right < left){
            return 0;
        }else if(left <= seg[cur].left && seg[cur].right <= right){
            return seg[cur].val;
        }else{
            return query(cur*2, left, right) + query(cur*2+1, left, right);
        }
    }
};