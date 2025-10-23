# Last updated: 23/10/2025, 1:06:21 pm
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, s))
        while len(s) > 2:
            new_s = []
            for i in range(1, len(s)):
                new_s.append((s[i] + s[i- 1]) % 10)
            s = new_s
        
        return s[0] == s[1]