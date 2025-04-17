# Last updated: 17/4/2025, 5:38:06 pm
mod = 10**9 + 7
class Solution:
    def createSortedArray(self, ins: List[int]) -> int:
        n = len(ins)
        m = n+1

        compression = {}
        index = 1
        for num in sorted(ins):
            if num not in compression:
                compression[num] = index
                index += 1

        def update(index):
            while index < m:
                tree[index] += 1
                index += index & (-index)
        
        def query(index):
            s = 0
            while index:
                s += tree[index]
                index -= index & (-index)
            return s

        tree = [0] * (n+1)
        cost = 0
        hash = defaultdict(int)

        for i, num in enumerate(ins):
            left = query(compression[num]-1)
            right = i - left - hash[num]
            
            cost = (cost + min(left, right)) % mod
            update(compression[num])
            hash[num] += 1
        
        return cost