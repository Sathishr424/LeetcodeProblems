# Last updated: 18/4/2025, 10:51:42 pm
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ret = [-1] * n

        for i in range(n*2 - 1):
            i %= n
            while stack and nums[stack[-1]] < nums[i]:
                ret[stack.pop()] = nums[i]
            
            stack.append(i)

        return ret
            
