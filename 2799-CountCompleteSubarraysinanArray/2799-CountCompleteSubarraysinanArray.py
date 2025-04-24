# Last updated: 24/4/2025, 9:13:46 am
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0

        uniq = {}
        for num in nums:
            uniq[num] = 1
        
        cnt = len(uniq)

        for i in range(n-cnt+1):
            uniq = {}
            for j in range(i, n):
                uniq[nums[j]] = 1
                if len(uniq) <= cnt: ret += len(uniq) == cnt
                else: break

        return ret