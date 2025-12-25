# Last updated: 12/25/2025, 7:10:51 PM
inf = float('inf')
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        # nums = [random.randrange(1, 1000000001) for _ in range(250)]
        n = len(nums)

        dp = [[-1] * (k + 1) for _ in range(n + 1)]
        
        def rec(index, rem):
            if dp[index][rem] != -1: return dp[index][rem]
            if index == n: 
                if rem == 0: return 0
                return inf
            if rem == 0: return inf
            xor = 0
            ans = inf
            for i in range(index, (n-rem+1)):
                xor ^= nums[i]
                ans = min(ans, max(xor, rec(i + 1, rem - 1)))
            dp[index][rem] = ans
            return ans

        ans = rec(0, k)
        return ans