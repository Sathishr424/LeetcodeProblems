# Last updated: 12/6/2025, 5:55:40 am
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ret = [0, 1]
    
        for i in range(1, n):
            left = i-1
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                l = right-left+1
                if l > ret[1]: ret = [left, l]
                left -= 1
                right += 1
            
            left = i-1
            right = i+1

            while left >= 0 and right < n and s[left] == s[right]:
                l = right-left+1
                if l > ret[1]: ret = [left, l]
                left -= 1
                right += 1

        return s[ret[0]:ret[0]+ret[1]]
