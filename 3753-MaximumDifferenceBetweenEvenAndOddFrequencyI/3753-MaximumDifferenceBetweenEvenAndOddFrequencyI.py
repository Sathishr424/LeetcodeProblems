# Last updated: 12/6/2025, 5:34:42 am
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        
        odd = 0
        even = 100
        for char in s:
            a = ord(char) - 97
            freq[a] += 1
        
        for cnt in freq:
            if cnt == 0: continue
            if cnt % 2 == 0:
                even = min(cnt, even)
            else:
                odd = max(cnt, odd)

        return odd - even
