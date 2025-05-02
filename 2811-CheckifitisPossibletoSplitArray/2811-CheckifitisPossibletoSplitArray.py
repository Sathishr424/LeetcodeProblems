# Last updated: 3/5/2025, 2:40:48 am
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2: return True

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        @cache
        def rec(l, r):
            if l == r: return 1
        
            if prefix[r+1] - prefix[l] >= m:
                return max(rec(l+1, r), rec(l, r-1)) + 1
            return 0

        return rec(0, n-1) == n