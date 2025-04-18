# Last updated: 14/4/2025, 6:02:20 pm
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        vis = {}
        for num in nums:
            vis[num] = 1
        
        ret = []
        n = len(nums)
        
        def rec(p):
            if len(p) == n:
                ret.append(p + [])
                return
            
            for num in nums:
                if vis[num]:
                    vis[num] = 0
                    p.append(num)
                    rec(p)
                    p.pop()
                    vis[num] = 1
        
        rec([])
        return ret