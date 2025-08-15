# Last updated: 15/8/2025, 10:56:40 pm
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []
        for i in range(n):
            index = bisect_left(stack, nums[i])
            if index < len(stack):
                stack[index] = nums[i]
            else:
                stack.append(nums[i])
            
        return len(stack)