# Last updated: 9/4/2025, 5:23:15 pm
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
        
        if len(stack) < k:
            return stack + nums[i+1:]
        
        return stack[:k]