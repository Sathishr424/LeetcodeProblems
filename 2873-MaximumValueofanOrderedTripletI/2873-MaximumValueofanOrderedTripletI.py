# Last updated: 2/4/2025, 11:36:55 am
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        
        stack = []
        maxi = -float('inf')

        for i in range(len(nums)):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            
            ret = max(ret, maxi * nums[i])

            if stack:
                maxi = max(stack[0] - nums[i], maxi)
            
            stack.append(nums[i])
        
        return ret if ret > 0 else 0
