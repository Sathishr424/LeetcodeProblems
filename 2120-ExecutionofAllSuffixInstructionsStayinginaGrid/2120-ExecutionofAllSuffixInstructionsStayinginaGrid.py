# Last updated: 20/6/2025, 10:36:11 am
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)

        pos = [[startPos[0], startPos[1]] for _ in range(m)]
        ret = [-1] * m
        
        for i in range(m):
            d = s[i]
            x = 0
            y = 0
            if d == 'L': x -= 1
            elif d == 'R': x += 1
            elif d == 'U': y -= 1
            elif d == 'D': y += 1
            for j in range(i+1):
                if ret[j] != -1: continue
                pos[j][0] += y
                pos[j][1] += x

                if pos[j][0] == n or pos[j][0] == -1 or pos[j][1] == -1 or pos[j][1] == n:
                    ret[j] = i-j
        
        for i in range(m):
            if ret[i] == -1:
                ret[i] = m-i
        
        return ret