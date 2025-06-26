# Last updated: 27/6/2025, 12:58:53 am
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0] * 58
        for char in s:
            freq[ord(char) - 65] += 1
        
        is_odd = 0
        ret = 0
        for i in range(58):
            if freq[i] % 2: 
                is_odd = 1
                ret += freq[i] - 1
            else:
                ret += freq[i]
        
        return ret + is_odd