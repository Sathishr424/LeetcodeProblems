# Last updated: 15/5/2025, 3:24:22 pm
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
            if index == 0: return []

            ans = []
            for i in range(index-1, -1, -1):
                if groups[index] != groups[i] and len(words[index]) == len(words[i]) and distance[i][index] == 1:
                    curr = dfs(i)
                    if len(curr) >= len(ans):
                        ans = curr + [words[i]]
            
            memo[index] = ans
            visited[index] = True
            return ans
        
        for i in range(n-1, -1, -1):
            ans = dfs(i)
            if len(ans) >= len(ret):
                ans.append(words[i])
                ret = ans

        return ret