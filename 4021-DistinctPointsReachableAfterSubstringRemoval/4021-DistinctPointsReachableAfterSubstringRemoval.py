# Last updated: 12/25/2025, 7:09:02 PM
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        x = 0
        y = 0

        def addPos(d):
            nonlocal x, y
            if d == 'U':
                y += 1
            elif d == 'D':
                y -= 1
            elif d == 'L':
                x -= 1
            else:
                x += 1
            
        def substractPos(d):
            nonlocal x, y
            if d == 'U':
                y -= 1
            elif d == 'D':
                y += 1
            elif d == 'L':
                x += 1
            else:
                x -= 1

        for i in range(n):
            addPos(s[i])
        
        for i in range(k):
            substractPos(s[i])

        uniq = {}
        uniq[(x, y)] = 1
        for i in range(k, n):
            addPos(s[i-k])
            substractPos(s[i])

            uniq[(x, y)] = 1

        return len(uniq)