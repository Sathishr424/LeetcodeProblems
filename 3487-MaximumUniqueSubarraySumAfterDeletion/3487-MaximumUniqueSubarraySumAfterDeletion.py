# Last updated: 25/7/2025, 12:42:25 pm
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        uniq = {}
        s = nums[0]
        uniq[nums[0]] = 1

        for i in range(1, len(nums)):
            num = nums[i]
            if num not in uniq and s + num > s:
                s += num
                uniq[num] = 1
        
        return s