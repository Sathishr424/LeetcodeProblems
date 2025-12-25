# Last updated: 12/25/2025, 7:09:36 PM
class SegmentTree:
    def __init__(self, n, compressed):
        self.n = n
        self.compressed = compressed
        self.tree = [0] * (self.n * 4)
        self.indexes = [0] * self.n

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.indexes[l] = index
            return
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)
    
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
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [nums[0]]
        maxi = nums[0]
        for i in range(1, n):
            maxi = max(maxi, nums[i])
            left.append(maxi)
        sl = SortedList()
        compressed = {}
        
        index = 0
        for num in sorted(nums):
            if num not in compressed:
                compressed[num] = index
                index += 1
        
        tree = SegmentTree(index, compressed)
        ret = [0] * n
        # print(left)
        for i in range(n-1, -1, -1):
            el = tree.query(0, index-1, 0, 0, max(compressed[nums[i]], compressed[left[i]]) - 1)
            
            ret[i] = max(el, left[i])
            tree.update(compressed[nums[i]], ret[i])
            
        # print(left)
        return ret