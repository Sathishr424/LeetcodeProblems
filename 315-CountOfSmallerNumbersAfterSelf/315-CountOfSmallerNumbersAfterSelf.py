# Last updated: 12/6/2025, 5:50:37 am
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)

        offset = min(nums)
        m = max(nums) - min(nums)
        
        tree = [0] * (m+1)
        ret = [0] * n

        def query(index):
            s = 0
            while index:
                s += tree[index]
                index -= index & -index
            return s
        
        def update(index):
            while index <= m:
                tree[index] += 1
                index += index & -index
        
        for i in range(n-1, -1, -1):
            ret[i] = query(nums[i]-offset)
            update(nums[i]-offset+1)
        
        return ret