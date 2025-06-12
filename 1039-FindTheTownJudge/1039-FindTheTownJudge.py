# Last updated: 12/6/2025, 5:44:34 am
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        trusted = defaultdict(int)

        for x, y in trust:
            trusted[y] += 1
            trusts[x] += 1
        
        for x in range(1, n+1):
            if trusted[x] == n-1 and trusts[x] == 0:
                return x
        
        return -1
        