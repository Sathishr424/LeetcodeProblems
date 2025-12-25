# Last updated: 12/25/2025, 7:08:01 PM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        st = str(n)
        ans = 0
        s = 0
        for d in st:
            if d != '0':
                ans = ans * 10 + int(d)
                s += int(d)

        return ans * s
        