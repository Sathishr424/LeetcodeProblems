# Last updated: 2/4/2025, 11:35:58 am
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        
        arr = [-float('inf')] * n
        stack = []
        maxi = -float('inf')

        for i in range(n):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            
            ret = max(ret, maxi * nums[i])

            if stack:
                arr[i] = stack[0] - nums[i]
                maxi = max(arr[i], maxi)
            stack.append(nums[i])
        
        return ret if ret > 0 else 0
