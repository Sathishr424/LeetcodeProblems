# Last updated: 9/4/2025, 5:19:11 pm
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1] > num:
                if (n - i) + len(stack) <= k: break
                stack.pop()
            
            stack.append(num)
        
        if len(stack) > k:
            while len(stack) > k: stack.pop()

        return stack