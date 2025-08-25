# Last updated: 25/8/2025, 9:55:18 pm
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (self.n * 4)
        self.indexes = [0] * self.n

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.indexes[l] = index
            return
        
        mid = (l + r) // 2
        self.build(l, mid, index * 2 + 1)
        self.build(mid + 1, r, index * 2 + 2)
    
    def query(self, l, r, index, left, right):
        if l > right or r < left:
            return 0
        
        if l >= left and r <= right:
            return self.tree[index]
        
        mid = (l + r) // 2

        return self.query(l, mid, index * 2 + 1, left, right) + self.query(mid + 1, r, index * 2 + 2, left, right)
    
    def update(self, index):
        index = self.indexes[index]
        self.tree[index] = 1

        while index:
            index = (index - 1) // 2
            self.tree[index] = self.tree[index * 2  + 1] + self.tree[index * 2 + 2]

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ret = 0

        indexes = [0] * n
        for i in range(n):
            indexes[nums1[i]] = i

        tree = SegmentTree(n)
        from_left = [0] * n
        for i in range(n):
            tree.update(indexes[nums2[i]])

            index = indexes[nums2[i]]
            # if index <= i:
            cnt = tree.query(0, n-1, 0, 0, index-1)
            from_left[i] = cnt
        
        for i in range(len(tree.tree)):
            tree.tree[i] = 0
        
        # from_right = [0] * n
        for i in range(n-1, -1, -1):
            tree.update(indexes[nums2[i]])

            index = indexes[nums2[i]]

            cnt = tree.query(0, n-1, 0, index + 1, n-1)
            ret += from_left[i] * cnt
            # from_right[i] = cnt
        
        # print(from_left)
        # print(from_right)

        return ret