# Last updated: 12/6/2025, 5:36:12 am
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

        dp = [0] * n
        prev = [n] * n

        max_index = 0
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if dp[j] > dp[i] and checkValid(i, j):
                    dp[i] = dp[j]
                    prev[i] = j
            
            dp[i] += 1
            
            if dp[i] > dp[max_index]:
                max_index = i
        
        ret = []
        i = max_index

        while i < n:
            ret.append(words[i])
            i = prev[i]

        return ret