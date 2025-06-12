# Last updated: 12/6/2025, 5:51:51 am
class Solution:
    def isHappy(self, n: int) -> bool:
        hash = {}
        while n > 1 and n not in hash:
            hash[n] = 1
            new = 0
            while n:
                val = n % 10
                n //= 10
                new += val ** 2
            n = new
        return n == 1
