# Last updated: 12/6/2025, 5:43:45 am
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        
        dp = [''] * (n+1)

        for i in range(1, m+1):
            prev = dp[0]
            for j in range(1, n+1):
                tmp = dp[j]
                if str1[i-1] == str2[j-1]:
                    dp[j] = prev + str1[i-1]
                else:
                    if len(dp[j-1]) > len(dp[j]):
                        dp[j] = dp[j-1]
                    else:
                        dp[j] = dp[j]
                prev = tmp
        
        i, j = 0, 0
        res = ''
        for c in dp[-1]:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1

        return res + str1[i:] + str2[j:]