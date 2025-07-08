# Last updated: 9/7/2025, 12:26:22 am
mod = 10**9 + 7
class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        totalSum = 0

        for i in range(n):
            l = i - left[i]
            r = right[i] - i
            
            totalSum += l * r * nums[i] % mod
            totalSum %= mod
        
        return totalSum
        