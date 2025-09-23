# Last updated: 24/9/2025, 12:28:17 am
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

        return max(self.query(l, mid, index * 2 + 1, left, right), self.query(mid + 1, r, index * 2 + 2, left, right))
    
    def update(self, index, new_val):
        index = self.indexes[index]
        self.tree[index] = new_val

        while index:
            index = (index - 1) // 2
            self.tree[index] = max(self.tree[index * 2  + 1], self.tree[index * 2 + 2])

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)

        max_num = max(nums) + 1
        segTree = SegmentTree(max_num)
        best = 1

        for i in range(n):
            num = nums[i]
            cnt = segTree.query(0, max_num-1, 0, max(0, num - k), num - 1) + 1
            best = max(best, cnt)
            segTree.update(num, cnt)
        
        return best