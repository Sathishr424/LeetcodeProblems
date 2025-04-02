# Last updated: 2/4/2025, 11:27:38 am
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ret = max((nums[i] - nums[j]) * nums[k], ret)
        
        return ret if ret > 0 else 0
