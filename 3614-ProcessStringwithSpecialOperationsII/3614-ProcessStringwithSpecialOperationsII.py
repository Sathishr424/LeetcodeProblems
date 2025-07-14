# Last updated: 14/7/2025, 5:32:15 pm
class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        total_cnt = 0
        new_s = {}

        for char in s:
            if char == '*':
                total_cnt = max(0, total_cnt - 1)
            elif char == '#':
                total_cnt += total_cnt
            elif char == '%':
                pass
            else:
                total_cnt += 1
                new_s[char] = 1
        
        if total_cnt <= k: return '.'

        index = k
        cnt = total_cnt

        for i in range(n-1, -1, -1):
            char = s[i]
            if char == '*':
                cnt += 1
            elif char == '#':
                cnt //= 2
                if index >= cnt:
                    index -= cnt
            elif char == '%':
                index = cnt - index - 1
            else:
                if index == cnt - 1: return char
                cnt -= 1