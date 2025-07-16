# Last updated: 16/7/2025, 8:55:39 am
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # nums = [random.randrange(1, 10**7 + 1) for _ in range(2 * 10**5)]
        n = len(nums)

        @cache
        def rec(index, to_match, balance):
            if index == n: return 0

            ans = rec(index + 1, to_match, balance)
            if (nums[index] + balance) % 2 == to_match:
                ans = max(ans, rec(index + 1, to_match, nums[index] % 2) + 1)
            return ans
        
        ans = max(rec(0, 0, 1), rec(0, 1, 0), rec(0, 0, 0), rec(0, 1, 1))
        
        rec.cache_clear()
        return ans