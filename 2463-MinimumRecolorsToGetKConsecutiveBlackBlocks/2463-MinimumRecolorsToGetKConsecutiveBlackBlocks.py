# Last updated: 12/6/2025, 5:37:58 am
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        for i in range(k):
            w += blocks[i] == 'W'
        
        ret = w

        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                w -= 1
            if blocks[i] == 'W':
                w += 1
            ret = min(w, ret)
        
        return ret
