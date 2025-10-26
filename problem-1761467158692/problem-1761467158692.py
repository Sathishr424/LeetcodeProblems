# Last updated: 26/10/2025, 1:55:58 pm
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