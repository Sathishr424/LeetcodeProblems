# Last updated: 7/15/2026, 12:02:09 PM
1def gcd(a, b):
2    rem = a % b
3    if rem == 0: return b
4    return gcd(b, rem)
5
6class Solution:
7    def gcdOfOddEvenSums(self, n: int) -> int:
8        return n
9        odd = 0
10        even = 0
11
12        for i in range(1, n * 2 + 1, 2):
13            odd += i
14        for i in range(2, n * 2 + 1, 2):
15            even += i
16
17        return gcd(odd, even)
18