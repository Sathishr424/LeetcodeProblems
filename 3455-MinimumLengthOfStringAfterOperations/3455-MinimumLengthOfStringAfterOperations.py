# Last updated: 12/6/2025, 5:35:35 am
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26

        for char in s:
            freq[ord(char) - 97] += 1
        
        ret = 0
        for i in range(26):
            if freq[i] == 0: continue
            if freq[i] % 2: ret += 1
            else: ret += 2
        
        return ret