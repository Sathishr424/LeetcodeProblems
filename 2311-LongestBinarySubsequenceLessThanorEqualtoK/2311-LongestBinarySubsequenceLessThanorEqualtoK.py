# Last updated: 26/6/2025, 9:26:10 pm
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        ans = [0, 1]
        for i in range(1, n):
            left = i-1
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            window = right - left
            if window > ans[1]:
                ans = [left, window]
            
            left = i-1
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            window = right - left
            if window > ans[1]:
                ans = [left, window]
        
        return s[ans[0]:ans[0] + ans[1]]