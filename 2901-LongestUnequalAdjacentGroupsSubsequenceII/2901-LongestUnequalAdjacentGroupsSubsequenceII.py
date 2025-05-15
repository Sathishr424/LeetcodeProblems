# Last updated: 15/5/2025, 4:17:24 pm
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        def checkValid(i, j):
            if len(words[i]) != len(words[j]) or groups[i] == groups[j]: return False
            change = False
            
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    if change: return False
                    change = True
            
            return change

        dp = [1 for i in range(n)]
        prev = [n] * n
        max_index = 0
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if dp[j] >= dp[i] and checkValid(i, j):
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > dp[max_index]:
                max_index = i
        
        ret = []
        i = max_index

        while i < n:
            ret.append(words[i])
            i = prev[i]

        return ret