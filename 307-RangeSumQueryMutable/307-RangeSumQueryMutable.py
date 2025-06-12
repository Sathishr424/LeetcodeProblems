# Last updated: 12/6/2025, 5:50:42 am
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(indexes, tree, index, left, right, arr):
    if left == right:
        indexes[left] = index
        tree[index] = arr[left]
        return tree[index]

    mid = (left+right) // 2

    tree[index] = build(indexes, tree, index*2+1, left, mid, arr) + build(indexes, tree, index*2+2, mid+1, right, arr)

    return tree[index]

def sumRange(tree, index, left, right, i, j):
    if i > right or j < left: return 0
    if i >= left and j <= right: return tree[index]

    mid = (i+j) // 2

    return sumRange(tree, index*2+1, left, right, i, mid) + sumRange(tree, index*2+2, left, right, mid+1, j)

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n*4)
        self.indexes = [0] * self.n
        build(self.indexes, self.tree, 0, 0, self.n-1, nums)

    def update(self, index: int, val: int) -> None:
        index = self.indexes[index]
        self.tree[index] = val

        while index > 0:
            index = (index-1) // 2
            self.tree[index] = self.tree[index*2+1] + self.tree[index*2+2]

    def sumRange(self, left: int, right: int) -> int:
        return sumRange(self.tree, 0, left, right, 0, self.n-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)