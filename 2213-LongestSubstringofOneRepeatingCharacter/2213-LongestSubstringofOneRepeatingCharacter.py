# Last updated: 4/9/2025, 4:01:40 am
class Node:
    def __init__(self):
        self.max = 1
        self.left = 1
        self.right = 1
        self.left_a = ''
        self.right_a = ''
        self.window = 1

class SegmentTree:
    def __init__(self, alp):
        self.alp = alp
        self.n = len(alp)
        self.tree = [Node() for _ in range(self.n * 4)]
        self.indexes = [0] * self.n

        self.build(0, self.n-1, 0)

    def assignTreeIndex(self, index, left, right):
        self.tree[index].left_a = left.left_a
        self.tree[index].right_a = right.right_a
        if left.right_a == right.left_a:
            max_cnt = left.right + right.left
            self.tree[index].max = max(left.max, right.max, max_cnt)
    
            if left.left == left.window:
                self.tree[index].left = max_cnt
            else:
                self.tree[index].left = left.left
    
            if right.right == right.window:
                self.tree[index].right = max_cnt
            else:
                self.tree[index].right = right.right
        else:
            self.tree[index].max = max(left.max, right.max)
    
            self.tree[index].left = left.left
            self.tree[index].right = right.right
    
    def build(self, l, r, index):
        if l == r:
            self.indexes[l] = index
            self.tree[index].left_a = self.alp[l]
            self.tree[index].right_a = self.alp[l]
            self.tree[index].l = l
            self.tree[index].r = l
            return self.tree[index]

        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.tree[index].window = left.window + right.window
        self.assignTreeIndex(index, left, right)

        return self.tree[index]
    
    def update(self, index, new_val):
        index = self.indexes[index]
        self.tree[index].left_a = new_val
        self.tree[index].right_a = new_val

        while index:
            index = (index - 1) // 2

            left = self.tree[index * 2  + 1]
            right = self.tree[index * 2  + 2]

            self.assignTreeIndex(index, left, right)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(queryCharacters)
        segTree = SegmentTree(s)
        ret = []
        for i in range(n):
            segTree.update(queryIndices[i], queryCharacters[i])

            ret.append(segTree.tree[0].max)

        return ret
        