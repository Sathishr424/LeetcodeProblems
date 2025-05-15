# Last updated: 15/5/2025, 4:01:42 pm
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        @cache
        def checkValid(i, j):
            if len(words[i]) != len(words[j]) or groups[i] == groups[j]: return False
            diff = 0
            
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]: 
                    diff += 1
            
            return diff == 1

        dp = [1 for i in range(n)]
        ret = 0
        
        for i in range(n-1, -1, -1):
            new_dp = dp[i]
            for j in range(i+1, n):
                if checkValid(i, j):
                    if dp[j] + dp[i] > new_dp:
                        new_dp = dp[i] + dp[j]
            
            dp[i] = new_dp
            if dp[i] > dp[ret]:
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