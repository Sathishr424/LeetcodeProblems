# Last updated: 4/5/2025, 9:00:57 am
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        (a, b)
        (c, d)
        """
        pairs = defaultdict(int)
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            
            key = f"{x},{y}"
            pairs[key] += 1

        ret = 0
        for pair in pairs:
            if pairs[pair] > 1:
                cnt = pairs[pair] - 1
                ret += cnt * (cnt+1) // 2
        
        return ret


