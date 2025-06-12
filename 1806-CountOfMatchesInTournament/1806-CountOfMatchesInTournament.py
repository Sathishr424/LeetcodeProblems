# Last updated: 12/6/2025, 5:40:16 am
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ret = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                ret += n
            else:
                n -= 1
                n //= 2
                ret += n
                n += 1
        
        return ret