# Last updated: 8/21/2026, 3:10:36 PM
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
12        mn = min(coins)
13        l = 1
14        r = mn * k + 1
15        while l < r:
16            mid = (l + r) // 2
17
18            curr = 0
19            for mask in range(1, 1 << n):
20                lcm_ = 1
21                cnt = 0
22                for i in range(n):
23                    if mask & (1 << i):
24                        lcm_ = lcm(lcm_, coins[i])
25                        cnt += 1
26
27                tmp = mid // lcm_
28                # print(bin(mask), lcm_, cnt, tmp)
29                if cnt % 2 == 0:
30                    curr -= mid // lcm_
31                else:
32                    curr += mid // lcm_
33
34            # print((l, r), mid, curr)
35            
36            if curr >= k:
37                r = mid
38            else:
39                l = mid + 1
40
41        return l