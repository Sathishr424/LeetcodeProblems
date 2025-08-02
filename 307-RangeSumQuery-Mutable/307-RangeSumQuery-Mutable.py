# Last updated: 2/8/2025, 7:47:19 pm
class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)
        self.indexes = [0] * self.n

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.indexes[l] = index
            self.tree[index] = self.nums[l]
            return self.tree[index]
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.tree[index] = left + right
        return self.tree[index]
    
    def query(self, l, r, index, left, right):
        if l > right or r < left:
            return 0
        
        if l >= left and r <= right:
            return self.tree[index]
        
        mid = (l + r) // 2

        return self.query(l, mid, index * 2 + 1, left, right) + self.query(mid + 1, r, index * 2 + 2, left, right)
    
    def update(self, index, new_val):
        index = self.indexes[index]
        self.tree[index] = new_val

        while index:
            index = (index - 1) // 2
            self.tree[index] = self.tree[index * 2  + 1] + self.tree[index * 2 + 2]

class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)
            
    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(0, self.tree.n-1, 0, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)