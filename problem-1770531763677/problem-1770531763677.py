# Last updated: 2/8/2026, 11:52:43 AM
1class Solution:
2    def mergeAdjacent(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4
5        stack = []
6        for num in nums:
7            stack.append(num)
8            while len(stack) > 1 and stack[-1] == stack[-2]:
9                stack.append(stack.pop() + stack.pop())
10
11        return stack