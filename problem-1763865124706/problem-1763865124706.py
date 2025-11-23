# Last updated: 23/11/2025, 8:02:04 am
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
        