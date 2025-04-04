# Last updated: 4/4/2025, 2:31:30 pm
cmax = lambda x, y: x if x > y else y

def getDirection(d, y, x):
    if d == 'N': return y-1, x
    if d == 'S': return y+1, x
    if d == 'W': return y, x-1
    if d == 'E': return y, x+1

def process(s, t, s2, t2, rem, st):
    res = 0
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
    return res

class Solution:
    def maxDistance(self, st: str, k: int) -> int:
        return max(process('S', 'N', 'W', 'E', k, st),
        process('S', 'N', 'E', 'W', k, st),
        process('N', 'S', 'E', 'W', k, st),
        process('N', 'S', 'W', 'E', k, st))
        

        
                    