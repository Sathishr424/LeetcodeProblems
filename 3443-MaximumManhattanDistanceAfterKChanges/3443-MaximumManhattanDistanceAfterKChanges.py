# Last updated: 4/4/2025, 2:24:23 pm
class Solution:
    def maxDistance(self, st: str, k: int) -> int:
        def getDirection(d):
            if d == 'N': return (-1, 0)
            if d == 'S': return (1, 0)
            if d == 'W': return (0, -1)
            if d == 'E': return (0, 1)

        res = 0

        def process(s, t, s2, t2, rem):
            nonlocal res
            x = 0
            y = 0
            for d in st:
                if rem > 0:
                    if d == s:
                        rem -= 1
                        d = t
                    elif d == s2:
                        rem -= 1
                        d = t2
                
                curr = getDirection(d)
                x += curr[0]
                y += curr[1]
                res = max(res, abs(x) + abs(y))
        
        process('S', 'N', 'W', 'E', k)
        process('S', 'N', 'E', 'W', k)
        process('N', 'S', 'E', 'W', k)
        process('N', 'S', 'W', 'E', k)

        return res        
        

        
                    