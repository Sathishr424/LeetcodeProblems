# Last updated: 15/4/2025, 5:30:43 pm
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            index = bisect_left(stack, num)
            if index < len(stack):
                stack[index] = num
            else:
                stack.append(num)
        
        return len(stack)