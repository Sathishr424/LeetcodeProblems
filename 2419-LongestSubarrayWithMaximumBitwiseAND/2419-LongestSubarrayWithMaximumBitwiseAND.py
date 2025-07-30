# Last updated: 30/7/2025, 7:44:13 am
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        max_num = max(nums)

        left = 0
        ret = 1
        for i in range(n):
            if nums[i] == max_num:
                if i > 0 and nums[i] == nums[i-1]:
                    ret = max(i - left + 1, ret)
                else:
                    left = i

        return ret