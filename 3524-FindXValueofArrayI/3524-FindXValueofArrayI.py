# Last updated: 9/22/2026, 2:38:55 AM
1class Solution:
2    def resultArray(self, nums: List[int], k: int) -> List[int]:
3        n = len(nums)
4        result = [0] * k
5        # Initial state: no elements have been processed, so no non-empty subarray exists.
6        dp = [0] * k
7
8        for i in range(n):
9            ndp = [0] * k  # Current state (rolling array).
10
11            ndp[nums[i] % k] += 1
12
13            for r in range(k):
14                ndp[(r * nums[i]) % k] += dp[r]
15
16            dp = ndp  # Update the state.
17
18            # Accumulate the answer.
19            for r in range(k):
20                result[r] += dp[r]
21        return result