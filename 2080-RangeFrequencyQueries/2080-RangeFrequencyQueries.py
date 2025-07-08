# Last updated: 8/7/2025, 7:22:21 pm
def build(tree, index, left, right, arr):
    if left == right:
        tree[index][arr[left]] = 1
        return tree[index]

    mid = (left+right) // 2

    left = build(tree, index*2+1, left, mid, arr)
    right = build(tree, index*2+2, mid+1, right, arr)
    
    for val in left:
        tree[index][val] += left[val]
    
    for val in right:
        tree[index][val] += right[val]
    
    return tree[index]

def query(tree, index, left, right, value, i, j):
    if j < left or i > right: return 0
    if i >= left and j <= right:
        return tree[index][value]

    mid = (i+j) // 2
    return query(tree, index*2+1, left, right, value, i, mid) + query(tree, index*2+2, left, right, value, mid+1, j)

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [defaultdict(int) for _ in range(self.n*4)]
        build(self.tree, 0, 0, self.n-1, arr)

    def query(self, left: int, right: int, value: int) -> int:
        return query(self.tree, 0, left, right, value, 0, self.n-1)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)