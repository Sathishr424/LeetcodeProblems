# Last updated: 17/4/2025, 5:41:52 pm
mod = 10**9 + 7
class Solution:
    def createSortedArray(self, ins: List[int]) -> int:
        m = max(ins)

        def update(index):
            while index <= m:
                tree[index] += 1
                index += index & (-index)
        
        def query(index):
            s = 0
            while index:
                s += tree[index]
                index -= index & (-index)
            return s

        tree = [0] * (m+1)
        cost = 0
        hash = defaultdict(int)

        for i, num in enumerate(ins):
            left = query(num-1)
            right = i - left - hash[num]

            cost = (cost + min(left, right)) % mod
            update(num)
            hash[num] += 1
        
        return cost