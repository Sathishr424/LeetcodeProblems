# Last updated: 4/26/2026, 8:29:54 PM
1
2class Solution:
3    def validDigit(self, n: int, x: int) -> bool:
4        num = n
5        while num >= 10:
6            num //= 10
7        if num == x: return False
8            
9        while n:
10            if n % 10 == x:
11                return True
12            n //= 10
13
14        return False
15