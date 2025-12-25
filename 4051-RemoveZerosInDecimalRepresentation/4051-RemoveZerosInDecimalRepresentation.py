# Last updated: 12/25/2025, 7:08:48 PM
class Solution:
    def removeZeros(self, n: int) -> int:
        ret = 0
        dig = 1

        while n:
            val = n % 10
            if val > 0:
                ret = val * dig + ret
                dig *= 10
            n //= 10

        return ret