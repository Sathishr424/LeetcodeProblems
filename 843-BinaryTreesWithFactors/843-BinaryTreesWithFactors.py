# Last updated: 12/6/2025, 5:46:17 am
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        hash = {}
        arr.sort()
        n = len(arr)
        dp = []
        for i in range(n): 
            hash[arr[i]] = i
            dp.append(1)
        for i in range(n):
            for j in range(i):
                x = arr[i]/arr[j]
                y = int(x)
                if x == y and y in hash:
                    dp[i] += dp[j] * dp[hash[y]]
        return sum(dp) % ((10**9) + 7)