# Last updated: 12/6/2025, 5:55:45 am
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        n = len(s)
        res = 0
        left = 0
        for i in range(n):
            char = s[i]

            if char in counts and counts[char] >= left:
                res = max(res, i-left)
                index = counts[char]
                
                left = index+1
            
            counts[char] = i
        
        return max(res, n-left)