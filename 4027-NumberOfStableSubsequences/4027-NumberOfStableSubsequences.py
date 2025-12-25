# Last updated: 12/25/2025, 7:09:01 PM
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        dp = [[[-1, -1] for _ in range(3)] for _ in range(n)]
        
        def rec(index, cnt, prev):
            if index == n: return 0
            if dp[index][cnt][prev] != -1:
                return dp[index][cnt][prev]
            ans = rec(index + 1, cnt, prev)

            p = nums[index] % 2
            if p == prev:
                if cnt + 1 < 2:
                    ans += rec(index + 1, cnt + 1, p) + 1
            else:
                ans += rec(index + 1, 0, p) + 1
            ans %= mod
            dp[index][cnt][prev] = ans
            return ans

        ans = 0
        for i in range(n):
            ans += rec(i + 1, 0, nums[i] % 2) + 1
            ans %= mod

        return ans