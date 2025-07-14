# Last updated: 14/7/2025, 5:32:45 pm
class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        cnt = 0

        for char in s:
            if char == '*':
                cnt = max(0, cnt - 1)
            elif char == '#':
                cnt += cnt
            elif char == '%':
                pass
            else:
                cnt += 1
        
        if cnt <= k: return '.'

        for i in range(n-1, -1, -1):
            char = s[i]
            if char == '*':
                cnt += 1
            elif char == '#':
                cnt //= 2
                if k >= cnt:
                    k -= cnt
            elif char == '%':
                k = cnt - k - 1
            else:
                if k == cnt - 1: return char
                cnt -= 1