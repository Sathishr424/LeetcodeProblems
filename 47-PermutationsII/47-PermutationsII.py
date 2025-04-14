# Last updated: 14/4/2025, 6:13:31 pm
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        vis = [1] * n

        ret = []
        def rec(p):
            if len(p) == n:
                ret.append(p + [])
                return
            
            prev = -11
            for i in range(n):
                if vis[i] and nums[i] != prev:
                    prev = nums[i]
                    vis[i] = 0
                    p.append(nums[i])
                    rec(p)
                    p.pop()
                    vis[i] = 1
        
        rec([])
        return ret