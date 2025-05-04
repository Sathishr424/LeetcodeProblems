# Last updated: 4/5/2025, 9:30:10 am
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = defaultdict(int)
        ret = 0
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            
            key = f"{x},{y}"
            ret += pairs[key]
            pairs[key] += 1
        
        return ret


