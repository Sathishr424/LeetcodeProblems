# Last updated: 12/6/2025, 5:39:26 am
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        left = first * second
        for num in nums:
            if num < first:
                second = first
                first = num
            elif num < second:
                second = num
        return left - (first * second)