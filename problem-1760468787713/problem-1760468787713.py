# Last updated: 15/10/2025, 12:36:27 am
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def rec(index):
            if index == n: return 0
            ans = inf
            uniq = defaultdict(int)
            trimmed = 0
            for i in range(index, n):
                uniq[nums[i]] += 1
                if uniq[nums[i]] == 2:
                    trimmed += 2
                elif uniq[nums[i]] > 2:
                    trimmed += 1
                ans = min(ans, rec(i + 1) + k + trimmed)

            return ans

        ans = rec(0)
        rec.cache_clear()
        return ans