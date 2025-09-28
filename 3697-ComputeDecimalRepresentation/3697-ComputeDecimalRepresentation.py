# Last updated: 28/9/2025, 11:41:49 am
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ret = []

        dig = 1
        while n:
            rem = n % 10
            if rem:
                ret.append(rem * dig)
            dig *= 10
            n //= 10

        return ret[::-1]