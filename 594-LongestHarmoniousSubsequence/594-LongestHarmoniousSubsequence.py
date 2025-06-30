# Last updated: 30/6/2025, 12:42:17 pm
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)

        ret = 0
        cnts = defaultdict(int)
        for i, num in enumerate(nums):
            cnts[num] += 1
            if cnts[num-1]:
                ret = max(ret, cnts[num-1] + cnts[num])
            if cnts[num+1]:
                ret = max(ret, cnts[num+1] + cnts[num])
        
        return ret
