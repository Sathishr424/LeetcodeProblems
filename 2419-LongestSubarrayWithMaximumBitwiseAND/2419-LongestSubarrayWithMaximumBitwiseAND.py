# Last updated: 30/7/2025, 7:45:27 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        max_num = max(nums)

        cnt = 0
        ret = 1
        for i in range(n):
            if nums[i] == max_num:
                if i > 0 and nums[i] == nums[i-1]:
                    cnt += 1
                    ret = cmax(cnt, ret)
                else:
                    cnt = 1

        return ret