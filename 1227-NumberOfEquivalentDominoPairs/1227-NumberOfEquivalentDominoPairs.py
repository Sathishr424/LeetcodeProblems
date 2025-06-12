# Last updated: 12/6/2025, 5:43:29 am
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = [[0] * 10 for _ in range(10)]
        ret = 0
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            
            ret += pairs[x][y]
            pairs[x][y] += 1
        
        return ret


