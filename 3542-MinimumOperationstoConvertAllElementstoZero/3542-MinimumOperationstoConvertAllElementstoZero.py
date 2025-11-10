# Last updated: 10/11/2025, 4:22:05 pm
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []
        op = 0
        def calcOp(num):
            nonlocal op
            prev = stack[-1]
            while stack and stack[-1] > num:
                curr = stack.pop()
                if curr != prev: op += 1
                prev = curr
            if prev > 0: op += 1

        for num in nums:
            if stack and stack[-1] > num:
                calcOp(num)
            
            stack.append(num)
        calcOp(0)
        return op
        