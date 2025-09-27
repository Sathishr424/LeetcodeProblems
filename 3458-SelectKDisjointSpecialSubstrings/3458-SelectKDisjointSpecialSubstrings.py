# Last updated: 28/9/2025, 2:22:00 am
class Node:
    def __init__(self):
        self.left = 0
        self.right = 0

class SegmentTree:
    def __init__(self, s, indexes):
        self.s = s
        self.n = len(s)
        self.indexes = indexes
        self.tree = [Node() for _ in range (self.n * 4)]

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.tree[index].left = self.indexes[self.s[l]][0]
            self.tree[index].right = self.indexes[self.s[l]][-1]
            return self.tree[index]
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.tree[index].left = min(left.left, right.left)
        self.tree[index].right = max(left.right, right.right)
        return self.tree[index]
    
    def query(self, l, r, index, left, right):
        if l > right or r < left:
            return True
        
        if l >= left and r <= right:
            return self.tree[index].left >= left and self.tree[index].right <= right
        
        mid = (l + r) // 2

        return self.query(l, mid, index * 2 + 1, left, right) and self.query(mid + 1, r, index * 2 + 2, left, right)

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0: return True
        n = len(s)

        indexes = defaultdict(list)

        for i in range(n):
            indexes[s[i]].append(i)

        segTree = SegmentTree(s, indexes)
        used = [0] * n
        for char in sorted(indexes.keys(), key=lambda x: indexes[x][-1] - indexes[x][0]):
            l = indexes[char][0]
            r = indexes[char][-1]

            i = l + 1
            while i < r:
                if indexes[s[i]][0] < l or used[indexes[s[i]][-1]]: break
                r = max(r, indexes[s[i]][-1])
                i += 1
            else:
                if r - l + 1 != n:
                    for i in range(l, r+1):
                        used[i] = 1
                    k -= 1
                    if k == 0: return True
        
        return False
