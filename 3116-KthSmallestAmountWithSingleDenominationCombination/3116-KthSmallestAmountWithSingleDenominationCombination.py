# Last updated: 8/21/2026, 3:12:18 PM
1class Solution:
2    def findKthSmallest(self, coins: List[int], k: int) -> int:
3        n = len(coins)
4        """
5        2, 4, 6, 8, 10, 12, 14, 16, 18, 20
6        3, 6, 9, 12, 15, 18, 21
7        6, 12, 18
8
9        2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21
10        """
11
12        l = 1
13        r = min(coins) * k + 1
14        while l < r:
15            mid = (l + r) // 2
16
17            curr = 0
18            for mask in range(1, 1 << n):
19                lcm_ = 1
20                cnt = 0
21                for i in range(n):
22                    if mask & (1 << i):
23                        lcm_ = lcm(lcm_, coins[i])
24                        cnt += 1
25
26                if cnt % 2:
27                    curr += mid // lcm_
28                else:
29                    curr -= mid // lcm_
30            
31            if curr >= k:
32                r = mid
33            else:
34                l = mid + 1
35
36        return l