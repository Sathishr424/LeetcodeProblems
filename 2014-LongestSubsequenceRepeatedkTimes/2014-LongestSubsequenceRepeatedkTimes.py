# Last updated: 27/6/2025, 10:02:11 pm
def charToInt(char):
    return ord(char) - 97

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        alps = [charToInt(char) for char in s]

        def rec(l, r):
            freq = [0] * 26
            for i in range(l, r+1):
                freq[alps[i]] += 1

            for i in range(l, r+1):
                if freq[alps[i]] < k:
                    return max(rec(l, i-1), rec(i+1, r))
            
            return r - l + 1
        
        return rec(0, n-1)