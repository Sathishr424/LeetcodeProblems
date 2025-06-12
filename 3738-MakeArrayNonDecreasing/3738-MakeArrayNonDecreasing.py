# Last updated: 12/6/2025, 5:34:49 am
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []

        for num in nums[::-1]:
            while stack and stack[-1] < num:
                stack.pop()

            stack.append(num)

        return len(stack)