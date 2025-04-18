# Last updated: 18/4/2025, 11:24:36 pm
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
        left = 0
        while left < n and greater[left] == inf and smaller[left] == inf:
            left += 1
        
        right = n-1
        while right >= 0 and greater[right] == inf and smaller[right] == inf:
            right -= 1
        
        return max(right-left+1, 0)

