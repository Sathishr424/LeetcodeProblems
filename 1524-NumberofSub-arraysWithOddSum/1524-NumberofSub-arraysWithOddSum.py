# Last updated: 11/15/2026, 10:49:26 AM
1class Solution:
2    def numOfSubarrays(self, nums: list[int]) -> int:
3        n = len(nums)
4        mod = 10**9 + 7
5
6        # odd -/+ odd = even 5 + 3 = 10
7        # odd -/+ even = odd 5 - 2 = 3
8        # even -/+ even = even 4 + 8 = 12
9
10        prefix = [0]
11        odds = [0] * (n + 1)
12        odd = 0
13        for i, num in enumerate(nums):
14            prefix.append(prefix[-1] + num)
15            curr = prefix[-1]
16
17            odd += curr % 2
18            odds[i] = odd
19
20        ans = 0
21        for i in range(n):
22            left = prefix[i]
23
24            odd = odds[n-1]
25            even = n - odd
26
27            if left % 2 == 0:
28                ans += odd - odds[i-1]
29            else:
30                ans += even - (i - odds[i-1]) 
31
32        return ans % mod