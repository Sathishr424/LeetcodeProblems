# Last updated: 12/6/2025, 5:38:38 am
class Solution:
    def mostPoints(self, ques: List[List[int]]) -> int:
        n = len(ques)

        dp = [-1] * (n+1)
        
        for i in range(n-1, -1, -1):
            b, s = ques[i]

            dp[i] = max(b, dp[i+s+1]+b if i+s+1 < n else -1, dp[i+1])
        
        return dp[0]