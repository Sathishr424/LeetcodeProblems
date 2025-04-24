# Last updated: 24/4/2025, 3:36:40 pm
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10: return []
        k = 10
        st = ''
        for i in range(k):
            st += s[i]
        visited = defaultdict(int)
        visited[st] += 1
        for i in range(k, n):
            st = s[i-k+1:i+1]
            visited[st] += 1
        ret = []
        for st in visited:
            if visited[st] > 1:
                ret.append(st)
        return ret