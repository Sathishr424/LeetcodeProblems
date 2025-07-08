# Last updated: 9/7/2025, 2:05:48 am
def getMinSubarraySum(nums):
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
        
        totalSum += l * r * nums[i]
    
    return totalSum

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min_ = getMinSubarraySum(nums)
        max_ = getMinSubarraySum([-num for num in nums]) * -1

        return max_ - min_