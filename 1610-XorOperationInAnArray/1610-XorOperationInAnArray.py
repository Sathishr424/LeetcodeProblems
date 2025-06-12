# Last updated: 12/6/2025, 5:41:19 am
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ret = 0
        for i in range(n):
            ret = ret^(start+(2*i))
        return ret