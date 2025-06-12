# Last updated: 12/6/2025, 5:47:57 am
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key=lambda x: x[1])
        ret = 0
        curr = -float('inf')
        for pair in pairs:
            if pair[0] > curr:
                ret += 1
                curr = pair[1]
        
        return ret

        