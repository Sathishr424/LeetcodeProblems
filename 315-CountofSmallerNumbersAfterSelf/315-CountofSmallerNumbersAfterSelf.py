# Last updated: 17/4/2025, 6:43:03 pm
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tree = [0] * (n+1)
        compression = {}
        index = 1
        ret = []

        for num in sorted(nums):
            if num not in compression:
                compression[num] = index
                index += 1
            ret.append(0)

        def query(index):
            s = 0
            while index:
                s += tree[index]
                index -= index & -index
            return s
        
        def update(index):
            while index <= n:
                tree[index] += 1
                index += index & -index
        
        for i in range(n-1, -1, -1):
            ret[i] = query(compression[nums[i]]-1)
            update(compression[nums[i]])
        
        return ret