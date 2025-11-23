# Last updated: 23/11/2025, 5:40:06 am
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def rec(index, rem):
            if index == n:
                if rem == 0: return 0
                return -inf

            ans = max(rec(index + 1, rem), rec(index + 1, (nums[index] + rem) % 3) + nums[index])
            return ans
        
        ans = max(0, rec(0, 0))
        rec.cache_clear()
        return ans