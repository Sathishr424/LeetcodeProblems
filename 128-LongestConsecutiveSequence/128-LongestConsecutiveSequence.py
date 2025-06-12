# Last updated: 12/6/2025, 5:52:40 am
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        relation = {}
    
        for num in nums:
            relation[num] = 0
        
        for num in relation:
            if num+1 in relation:
                relation[num] = 1
        ret = 1
        vis = {}

        def helper(num):
            if num in vis: return vis[num]
            elif num in relation and relation[num]:
                cnt = helper(num+1) + 1
                vis[num] = cnt
                return cnt
            return 0
        
        for num in relation:
            if not relation[num]: continue
            cnt = helper(num+1) + 2
            ret = max(cnt, ret)
        return ret
            
