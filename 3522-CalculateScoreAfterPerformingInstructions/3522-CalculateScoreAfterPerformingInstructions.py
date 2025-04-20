# Last updated: 21/4/2025, 12:14:18 am
class Solution:
    def calculateScore(self, ins: List[str], values: List[int]) -> int:
        score = 0
        vis = {}
        n = len(ins)
        i = 0
        while i >= 0 and i < n:
            if i in vis: break
            vis[i] = 1
            if ins[i] == 'jump':
                i = i + values[i]
                continue
            else:
                score += values[i]
            i += 1
        return score