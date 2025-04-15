# Last updated: 15/4/2025, 9:17:21 pm
class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        # Count of numbers <= i-1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        offset = {v: i for i, v in enumerate(sorted(set(nums)))}
        bit = BIT(len(offset))
        res = []

        for num in reversed(nums):
            idx = offset[num]
            res.append(bit.query(idx))  # Count of smaller numbers
            bit.update(idx, 1)          # Insert this number

        return res[::-1]
