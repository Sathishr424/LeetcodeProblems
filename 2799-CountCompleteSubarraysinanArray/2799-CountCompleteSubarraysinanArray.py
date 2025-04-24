# Last updated: 24/4/2025, 9:08:09 am
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)

        uniq = {}
        for num in nums:
            uniq[num] = 1
        
        cnt = len(uniq)

        for i in range(n):
            uniq = {}
            for j in range(i, n):
                uniq[nums[j]] = 1
                if len(uniq) == cnt: ret += 1

        return ret