# Last updated: 24/4/2025, 3:37:14 pm
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10: return []
        k = 10
        visited = defaultdict(int)
        visited[s[:10]] += 1
        for i in range(k, n):
            visited[s[i-k+1:i+1]] += 1
        ret = []
        for st in visited:
            if visited[st] > 1:
                ret.append(st)
        return ret