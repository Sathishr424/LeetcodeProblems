# Last updated: 10/8/2025, 4:24:30 am
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0
        while c or a or b:
            rem = c % 2
            if rem == 0:
                if a % 2:
                    ret += 1
                if b % 2:
                    ret += 1
            elif (a % 2) + (b % 2) == 0:
                ret += 1
            
            c //= 2
            a //= 2
            b //= 2
        
        return ret