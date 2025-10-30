# Last updated: 30/10/2025, 9:54:14 pm
class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.ones = [0] * (self.n * 4)
        self.lazy = [0] * (self.n * 4)
        self.all_ones = sum(nums)
        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.ones[index] = self.nums[l]
            return self.ones[index]
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.ones[index] = left + right
        return self.ones[index]

    def extendLazy(self, index, l, mid, r):
        if self.lazy[index]:
            left = index * 2 + 1
            right = index * 2 + 2

            self.ones[left] = (mid - l + 1) - self.ones[left]
            self.ones[right] = (r - mid) - self.ones[right]
            self.lazy[left] ^= 1
            self.lazy[right] ^= 1

            self.lazy[index] = 0
    
    def update(self, l, r, index, left, right):
        if l > right or r < left:
            return
        
        if l >= left and r <= right:
            old_ones = self.ones[index]
            new_ones = (r - l + 1) - self.ones[index]
            
            self.all_ones += new_ones - old_ones
            
            self.ones[index] = new_ones
            self.lazy[index] ^= 1
            return
        
        mid = (l + r) // 2

        self.extendLazy(index, l, mid, r)

        self.update(l, mid, index * 2 + 1, left, right)
        self.update(mid + 1, r, index * 2 + 2, left, right)
        self.ones[index] = self.ones[index * 2 + 1] + self.ones[index * 2 + 2]

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)

        segTree = SegmentTree(nums1)
        totalSum = sum(nums2)
        ret = []

        for t, l, r in queries:
            if t == 1:
                segTree.update(0, n-1, 0, l, r)
            elif t == 2:
                totalSum += segTree.all_ones * l
            else:
                ret.append(totalSum)

        return ret