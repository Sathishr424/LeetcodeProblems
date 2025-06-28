# Last updated: 28/6/2025, 8:48:41 am
def charToInt(char):
    return ord(char) - 97

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        freq = [0] * 26
        for char in s:
            freq[charToInt(char)] += 1
        
        odd = 0
        for i in range(26):
            odd += freq[i] % 2

        return odd <= k