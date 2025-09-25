# Last updated: 26/9/2025, 2:32:23 am
class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.tree[index] = self.nums[l]
            return self.tree[index]
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.tree[index] = max(left, right)
        return self.tree[index]
    
    def query(self, l, r, index, left, val):
        if r < left or self.tree[index] <= val:
            return self.n

        if l == r:
            return l
        
        mid = (l + r) // 2

        ans = self.query(l, mid, index * 2 + 1, left, val)
        if ans == self.n:
            return self.query(mid + 1, r, index * 2 + 2, left, val)
        return ans
    
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        segTree = SegmentTree(nums)

        ret = []
        for i in range(n):
            index = segTree.query(0, n-1, 0, i + 1, nums[i])
            if index != n:
                index = segTree.query(0, n-1, 0, index + 1, nums[i])

            if index != n:
                ret.append(nums[index])
            else:
                ret.append(-1)

        return ret