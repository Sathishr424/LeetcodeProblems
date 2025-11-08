# Last updated: 9/11/2025, 1:42:15 am
class Solution:
    def splitNum(self, num: int) -> int:
        nums = [int(d) for d in str(num)]
        nums.sort(reverse=True)

        left = 0
        right = 0

        while nums:
            left = left * 10 + nums.pop()
            if nums:
                right = right * 10 + nums.pop()

        return left + right