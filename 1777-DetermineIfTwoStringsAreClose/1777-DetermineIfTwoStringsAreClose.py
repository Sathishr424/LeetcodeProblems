# Last updated: 12/6/2025, 5:40:28 am
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m = len(word1)
        n = len(word2)

        if m != n: return False

        counts = {}

        for char in word1:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        bu = {}

        for char in word2:
            if char not in counts: return False
            if char in bu:
                bu[char] += 1
            else:
                bu[char] = 1
        
        if len(bu) != len(counts): return False
        
        counts = sorted(list(counts.values()))
        bu = sorted(list(bu.values()))

        for i in range(len(counts)):
            if bu[i] != counts[i]: return False
        
        return True