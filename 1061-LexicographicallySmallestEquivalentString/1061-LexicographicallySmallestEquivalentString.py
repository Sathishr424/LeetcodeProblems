# Last updated: 5/6/2025, 1:18:16 pm
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        graph = defaultdict(list)

        for i in range(n):
            if s1[i] != s2[i]:
                graph[s1[i]].append(s2[i])
                graph[s2[i]].append(s1[i])
        
        visited = {}

        def dfs(char, vis):
            if char in visited: return visited[char]
            ans = char
            for new_char in graph[char]:
                if new_char not in vis:
                    vis[new_char] = 1
                    ans = min(ans, dfs(new_char, vis))
            return ans

        ret = ''
        for char in baseStr:
            ret += dfs(char, {char: 1})
        
        return ret