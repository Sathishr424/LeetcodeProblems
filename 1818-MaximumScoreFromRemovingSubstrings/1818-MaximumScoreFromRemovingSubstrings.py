# Last updated: 12/6/2025, 5:40:12 am
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        a = 0
        b = 0
        ret = 0
        if y > x:
            for i in range(n):
                if s[i] == 'a':
                    if b > 0:
                        ret += y
                        b -= 1
                    else: a += 1
                elif s[i] == 'b': b += 1
                else:
                    ret += min(a, b) * x
                    a = 0
                    b = 0
            ret += min(a, b) * x
        else:
            for i in range(n):
                if s[i] == 'a': a += 1
                elif s[i] == 'b':
                    if a > 0:
                        ret += x
                        a -= 1
                    else: b += 1
                else:
                    ret += min(a, b) * y
                    a = 0
                    b = 0
            ret += min(a, b) * y
        return ret
