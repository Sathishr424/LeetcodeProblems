# Last updated: 15/5/2025, 4:08:32 pm
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        memo = [[None] * n for _ in range(n)]

        def checkValid(i, j):
            if memo[i][j] != None: return memo[i][j]
            memo[i][j] = False
            if len(words[i]) != len(words[j]) or groups[i] == groups[j]: return False
            change = False
            
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    if change: return False
                    change = True
            
            memo[i][j] = change
            return change

        dp = [1 for i in range(n)]
        ret = 0
        
        for i in range(n-1, -1, -1):
            new_l = dp[i]
            for j in range(i+1, n):
                if checkValid(i, j) and dp[j] + dp[i] > new_l:
                    new_l = dp[i] + dp[j]
            
            dp[i] = new_l
            if new_l > dp[ret]:
                ret = i
        
        arr = [words[ret]]
        rem = dp[ret] - 1
        prev = ret
        
        for i in range(ret+1, n):
            if dp[i] == rem and checkValid(prev, i):
                prev = i
                rem -= 1
                arr.append(words[i])

        return arr