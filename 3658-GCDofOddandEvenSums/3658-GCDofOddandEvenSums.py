# Last updated: 7/15/2026, 12:01:47 PM
1def gcd(a, b):
2    rem = a % b
3    if rem == 0: return b
4    return gcd(b, rem)
5
6class Solution:
7    def gcdOfOddEvenSums(self, n: int) -> int:
8        odd = 0
9        even = 0
10
11        for i in range(1, n * 2 + 1, 2):
12            odd += i
13        for i in range(2, n * 2 + 1, 2):
14            even += i
15
16        return gcd(odd, even)
17