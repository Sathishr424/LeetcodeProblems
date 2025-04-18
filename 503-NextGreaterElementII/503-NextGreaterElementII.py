# Last updated: 18/4/2025, 10:49:30 pm
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ret = [-1] * n

        for i in range(n*2 - 1):
            i %= n
            while stack and stack[-1][0] < nums[i]:
                ret[stack.pop()[1]] = nums[i]
            
            stack.append((nums[i], i))

        return ret
            
