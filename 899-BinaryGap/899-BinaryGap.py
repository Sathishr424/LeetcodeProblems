# Last updated: 12/6/2025, 5:45:51 am
class Solution:
    def binaryGap(self, n: int) -> int:
        prev = None
        index = 0
        ret = 0
        while n:
            if n % 2:
                if prev != None:
                    ret = max(ret, index - prev)
                prev = index
            n //= 2
            index += 1
        return ret