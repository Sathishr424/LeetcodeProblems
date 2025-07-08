# Last updated: 9/7/2025, 12:29:49 am
mod = 10**9 + 7
class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = []
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack: left.append(stack[-1])
            else: left.append(-1)
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
            totalSum = (totalSum + ((i - left[i]) * (right[i] - i) * nums[i] % mod)) % mod
        
        return totalSum
        