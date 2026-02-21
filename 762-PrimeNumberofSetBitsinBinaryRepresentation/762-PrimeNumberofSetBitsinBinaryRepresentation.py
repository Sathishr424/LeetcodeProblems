# Last updated: 2/21/2026, 11:21:55 PM
1primes = {2, 3, 5, 7, 11, 13, 17, 19}
2class Solution:
3    def countPrimeSetBits(self, left: int, right: int) -> int:
4        cnt = 0
5        for num in range(left, right+1):
6            bits = 0
7            while num:
8                bits += num & 1
9                num >>= 1
10            cnt += bits in primes
11        
12        return cnt
13        