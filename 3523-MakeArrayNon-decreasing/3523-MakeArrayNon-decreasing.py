# Last updated: 21/4/2025, 12:14:29 am
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []

        for num in nums[::-1]:
            while stack and stack[-1] < num:
                stack.pop()

            stack.append(num)

        return len(stack)