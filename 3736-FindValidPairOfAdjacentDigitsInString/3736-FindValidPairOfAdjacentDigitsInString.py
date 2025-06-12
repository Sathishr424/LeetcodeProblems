# Last updated: 12/6/2025, 5:34:50 am
class Solution:
    def findValidPair(self, s: str) -> str:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if freq[s[i]] == int(s[i]) and freq[s[i-1]] == int(s[i-1]):
                    return s[i-1] + s[i]
        
        return ''
