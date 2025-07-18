# Last updated: 12/6/2025, 5:54:32 am
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        vis = [1] * n

        ret = []
        def rec(p):
            if len(p) == n:
                return ret.append(list(p))
            
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