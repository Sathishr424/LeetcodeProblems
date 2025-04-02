# Last updated: 2/4/2025, 11:34:12 am
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        
        arr = [-float('inf')] * n
        stack = []

        for i in range(n):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            
            if stack:
                arr[i] = stack[0] - nums[i]
            stack.append(nums[i])

        for i in range(n):
            for j in range(i+1, n):
                ret = max(arr[i] * nums[j], ret)
        
        return ret if ret > 0 else 0
