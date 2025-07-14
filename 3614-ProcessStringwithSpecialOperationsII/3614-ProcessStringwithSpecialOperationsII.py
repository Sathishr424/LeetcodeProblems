# Last updated: 14/7/2025, 12:14:50 pm
class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        total_cnt = 0

        for char in s:
            if char == '*':
                total_cnt = max(0, total_cnt - 1)
            elif char == '#':
                total_cnt += total_cnt
            elif char == '%':
                pass
            else:
                total_cnt += 1
        
        if total_cnt <= k: return '.'

        def checkMatch(a):
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
                    if index == cnt - 1 and char == a: return True
                    cnt -= 1

                if index >= cnt: return False
            
            return True

        for i in range(26):
            a = chr(ord('a') + i)
            if checkMatch(a): return a