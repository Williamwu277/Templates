class Node:

    def __init__(self, left, right, val): self.left, self.right, self.val = left, right, val


class SegmentTree:

    def __init__(self, size, arr):
        self.seg, self.arr = [Node(0, 0, 0) for _ in range((size+1) * 4)], arr
        self.build(1, 1, len(arr)-1)

    def build(self, cur, left, right):
        if left == right: self.seg[cur] = Node(left, right, self.arr[left])
        else:
            mid = (left + right) // 2
            self.build(cur * 2, left, mid)
            self.build(cur * 2 + 1, mid + 1, right)
            self.seg[cur] = Node(left, right, self.seg[cur * 2].val + self.seg[cur * 2 + 1].val)

    def query(self, cur, left, right):
        if left > self.seg[cur].right or right < self.seg[cur].left: return 0
        elif left <= self.seg[cur].left and self.seg[cur].right <= right: return self.seg[cur].val
        else: return self.query(cur * 2, left , right) + self.query(cur * 2 + 1, left, right)

    def update(self, cur, index, val):
        if self.seg[cur].left == index and self.seg[cur].right == index: self.seg[cur].val = val
        else:
            mid = (self.seg[cur].left + self.seg[cur].right) // 2
            if index <= mid: self.update(cur * 2, index, val)
            else: self.update(cur * 2 + 1, index, val)
            self.seg[cur].val = self.seg[cur * 2].val + self.seg[cur * 2 + 1].val
