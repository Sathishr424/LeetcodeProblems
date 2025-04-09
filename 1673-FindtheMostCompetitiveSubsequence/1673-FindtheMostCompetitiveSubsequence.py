# Last updated: 9/4/2025, 5:22:00 pm
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            exit_ = False
            while stack and stack[-1] > num:
                if (n - i) + len(stack) <= k:
                    exit_ = True
                    break
                stack.pop()
            
            stack.append(num)
            if exit_: break
        
        if len(stack) > k:
            while len(stack) > k: stack.pop()
            return stack
        else:
            return stack + nums[i+1:]