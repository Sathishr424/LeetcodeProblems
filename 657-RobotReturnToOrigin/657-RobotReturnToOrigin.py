# Last updated: 12/6/2025, 5:47:51 am
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for m in moves:
            if m in 'UD':
                y += -1 if m == 'U' else 1
            elif m in 'LR':
                x += -1 if m == 'L' else 1
        
        return x == y and x == 0