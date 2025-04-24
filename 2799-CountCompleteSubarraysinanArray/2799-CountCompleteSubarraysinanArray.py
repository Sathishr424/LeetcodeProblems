# Last updated: 24/4/2025, 9:08:43 am
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0

        uniq = {}
        for num in nums:
            uniq[num] = 1
        
        cnt = len(uniq)

        for i in range(n):
            uniq = {}
            for j in range(i, n):
                uniq[nums[j]] = 1
                if len(uniq) == cnt: ret += 1
                elif len(uniq) > cnt: break

        return ret