# Last updated: 4/4/2025, 2:29:01 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxDistance(self, st: str, k: int) -> int:
        def getDirection(d, y, x):
            if d == 'N': return y-1, x
            if d == 'S': return y+1, x
            if d == 'W': return y, x-1
            if d == 'E': return y, x+1

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
                
                x, y = getDirection(d, x, y)
                res = cmax(res, abs(x) + abs(y))
        
        process('S', 'N', 'W', 'E', k)
        process('S', 'N', 'E', 'W', k)
        process('N', 'S', 'E', 'W', k)
        process('N', 'S', 'W', 'E', k)

        return res        
        

        
                    