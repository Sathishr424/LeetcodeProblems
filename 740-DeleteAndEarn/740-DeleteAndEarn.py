# Last updated: 12/6/2025, 5:47:14 am
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hash = defaultdict(lambda: 0)

        for n in nums:
            hash[n] += 1
        
        arr = sorted(list(hash.keys()))
        n = len(arr)
        dp = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            val = arr[i-1] * hash[arr[i-1]]
            if i-2 >= 0:
                if arr[i-2]+1 == arr[i-1]:
                    dp[i] = max(dp[i-1], dp[i-2] + val)
                else:
                    dp[i] = max(dp[i-1], dp[i-2]) + val
            else:
                dp[i] = val

        return dp[-1]
        