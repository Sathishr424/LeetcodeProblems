# Last updated: 12/6/2025, 5:33:45 am
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ret = 0

        for num in nums:
            prev = -1
            while stack and stack[-1] > num:
                p = stack.pop()
                ret += p != prev
                prev = p
            stack.append(num)

        prev = -1
        for num in stack:
            if num == prev or num == 0: continue
            ret += 1
            prev = num

        return ret

            