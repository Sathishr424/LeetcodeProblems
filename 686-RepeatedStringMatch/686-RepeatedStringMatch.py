# Last updated: 24/6/2025, 5:55:56 pm
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)

        new_a = a + (a * ceil(m / n))

        def getKMP(word):
            n = len(word)
            lps = [0] * n
            
            i = 1
            j = 0
            while i < n:
                if word[i] == word[j]:
                    j += 1
                    lps[i] = j
                elif j > 0:
                    j = lps[j - 1]
                    continue
                i += 1
            return lps
        
        lps = getKMP(b)
        j = 0
        i = 0
        while i < len(new_a):
            if new_a[i] == b[j]:
                j += 1
            elif j > 0:
                j = lps[j - 1]
                continue
            if j == len(b): return i // n + 1
            i += 1
        return -1
