# Last updated: 12/6/2025, 5:52:51 am
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1 for i in range(rowIndex+1)]
        for i in range(2, rowIndex+1):
            prev = dp[0]
            for j in range(1,i):
                tmp = dp[j]
                dp[j] += prev
                prev = tmp
        return dp