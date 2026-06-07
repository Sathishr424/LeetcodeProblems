# Last updated: 6/7/2026, 2:40:25 PM
1class Solution:
2    def consecutiveSetBits(self, n: int) -> bool:
3        prev = 0
4        cnt = 0
5        while n:
6            curr = n & 1
7            if curr == 1 and curr == prev:
8                cnt += 1
9            prev = curr
10            n >>= 1
11        return cnt == 1
12        
13