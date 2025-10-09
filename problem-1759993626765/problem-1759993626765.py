# Last updated: 9/10/2025, 12:37:06 pm
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1

        return max(pos, neg)