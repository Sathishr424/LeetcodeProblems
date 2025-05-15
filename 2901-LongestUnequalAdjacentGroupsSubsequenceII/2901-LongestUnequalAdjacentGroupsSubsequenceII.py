# Last updated: 15/5/2025, 3:16:50 pm
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        distance = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if len(words[i]) != len(words[j]): continue
                diff = 0
                
                for k in range(len(words[i])):
                    if words[i][k] != words[j][k]: diff += 1
                
                distance[i][j] = diff

        memo = [[] for _ in range(n)]
        visited = [False] * n
        ret = []

        def dfs(index):
            if visited[index]: return memo[index]
            if index == n: return []

            ans = []
            for i in range(index+1, n):
                if groups[index] != groups[i] and len(words[index]) == len(words[i]) and distance[index][i] == 1:
                    curr = [words[i]] + dfs(i)
                    if len(curr) > len(ans):
                        ans = curr
            memo[index] = ans
            visited[index] = True
            return ans
        
        for i in range(n):
            ans = [words[i]] + dfs(i)
            if len(ans) > len(ret):
                ret = ans

        return ret