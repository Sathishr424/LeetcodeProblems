# Last updated: 11/5/2025, 6:26:42 pm
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        dp = [[0] * 26 for _ in range(26)]
        arr = [ord(char) - 97 for char in s]
        ret = 0
        
        right = [0] * 26
        for i in range(n):
            right[arr[i]] += 1
        
        left = [0] * 26
        for i in range(n):
            a = arr[i]
            right[a] -= 1
            for num in range(26):
                if dp[num][a] == 0 and left[num] and right[num]:
                    ret += 1
                    dp[num][a] = 1
            left[a] += 1

        return ret