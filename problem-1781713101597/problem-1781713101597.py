# Last updated: 6/17/2026, 9:48:21 PM
1class Solution:
2    def sumOfGoodIntegers(self, n: int, k: int) -> int:
3        ans = 0
4        for i in range(max(1, n-k-1), n+k+1):
5            if abs(n - i) <= k and (n & i) == 0:
6                ans += i
7
8        return ans
9
10        
11