# Last updated: 15/5/2025, 3:50:42 pm
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

        dp = [[words[i]] for i in range(n)]
        ret = dp[0]
        
        for i in range(n-1, -1, -1):
            new_dp = dp[i]
            for j in range(i+1, n):
                if len(words[i]) == len(words[j]) and groups[i] != groups[j] and distance[i][j] == 1:
                    if len(dp[j]) + len(dp[i]) > len(new_dp):
                        new_dp = dp[i] + dp[j]
            
            dp[i] = new_dp
            if len(new_dp) > len(ret):
                ret = new_dp

        return ret