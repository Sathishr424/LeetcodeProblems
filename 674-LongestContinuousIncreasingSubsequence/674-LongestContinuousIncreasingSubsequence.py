# Last updated: 12/6/2025, 5:47:44 am
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        prev = -float('inf')
        curr = 0
        for num in nums:
            if num > prev:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
            prev = num
        return ans