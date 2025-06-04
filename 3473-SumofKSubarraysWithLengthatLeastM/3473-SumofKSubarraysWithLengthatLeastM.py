# Last updated: 4/6/2025, 10:34:37 pm
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        inf = float('inf')

        dp = [[[-inf, -inf] for _ in range(k+1)] for _ in range(n+1)]
        
        def rec(index, k, expand):
            if dp[index][k][expand] != -inf: return dp[index][k][expand]
            if k == 0 and (expand == 0 or index == n): return 0

            ans = -inf
            if index+1 <= n-(k*m):
                ans = rec(index+1, k, 0)
            
            if expand and index+1 <= n-(k*m):
                ans = max(ans, rec(index+1, k, 1) + nums[index])
            if k > 0:
                t = prefix[index+m] - prefix[index]

                ans = max(ans, rec(index+m, k-1, 1) + t)
            dp[index][k][expand] = ans
            return ans
        
        ans = rec(0, k, 0)
        return ans