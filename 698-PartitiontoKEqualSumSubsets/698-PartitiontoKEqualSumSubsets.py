# Last updated: 13/7/2025, 1:07:56 am
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        stack = []

        for i in range(n):
            index = bisect_left(stack, nums[i])
            if index == len(stack):
                stack.append(nums[i])
            else:
                stack[index] = nums[i]
        
        return len(stack)