# Last updated: 24/4/2025, 3:45:10 pm
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10: return []
        k = 10
        visited = defaultdict(int)
        for i in range(n-k+1):
            visited[s[i:i+k]] += 1
        ret = []
        for st in visited:
            if visited[st] > 1:
                ret.append(st)
        return ret