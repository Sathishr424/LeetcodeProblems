# Last updated: 8/9/2025, 12:39:35 pm
class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                if i - index + 1 >= 3:
                    count += 1

            if stack and i - stack[-1] + 1 >= 3:
                count += 1
            stack.append(i)

        return count    
        