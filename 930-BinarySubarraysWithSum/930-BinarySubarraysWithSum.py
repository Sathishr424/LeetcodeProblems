# Last updated: 26/4/2025, 2:32:33 am
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        s = 0
        """
        [1,0,1,0,1]
        """
        ret = 0
        prefix = [0] * (n+1)
        prefix[0] = 1
        s = 0

        for num in nums:
            s += num

            ret += prefix[s-goal]
            prefix[s] += 1
        
        return ret