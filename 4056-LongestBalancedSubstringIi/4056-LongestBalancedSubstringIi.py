# Last updated: 12/25/2025, 7:08:42 PM
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        best = 1
        prev = s[0]
        cnt = 1
        for i in range(1, n):
            if s[i] == prev:
                cnt += 1
            else:
                prev = s[i]
                cnt = 1
            best = max(best, cnt)
        
        for sub in ['ab', 'bc', 'ac']:
            diff = {0: 0}
            x = 0
            y = 0
            for i in range(n):
                if s[i] not in sub:
                    diff = {0: 0}
                    x = 0
                    y = 0
                else:
                    if s[i] == sub[0]:
                        x += 1
                    else:
                        y += 1
                    curr = x - y
                    if curr in diff:
                        best = max(best, (x - diff[curr]) * 2)
                    else:
                        diff[curr] = x
        a = 0
        b = 0
        c = 0
        diff = {}
        diff[(0,0)] = 0
        for i in range(n):
            if s[i] == 'a': a += 1
            elif s[i] == 'b': b += 1
            else: c += 1

            x = a - b
            y = b - c
            if (x, y) in diff:
                best = max(best, (a - diff[(x, y)]) * 3)
            else:
                diff[(x, y)] = a
        
        return best