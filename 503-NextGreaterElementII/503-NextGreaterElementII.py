# Last updated: 18/4/2025, 11:16:23 pm
inf = float('inf')
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        greater = [inf] * n
        smaller = [inf] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                smaller[stack.pop()] = nums[i]
            
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                greater[stack.pop()] = nums[i]
            
            stack.append(i)
        
        ret = 0
        for i in range(n):
            if greater[i] != inf or smaller[i] != inf: break
        
        left = i
        for i in range(n-1, -1, -1):
            if greater[i] != inf or smaller[i] != inf: return i-left+1
        
        return 0

