# Last updated: 12/8/2025, 12:58:02 am
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        base = 31
        mod = 10**9 + 7
        mp = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

        freq = defaultdict(int)
        ret = []

        for i in range(n-9):
            h = 0
            p = 0
            for j in range(i, i + 10):
                a = mp[s[j]]
                h = h + (a * pow(base, p, mod) % mod)
                h %= mod
                p += 1
            freq[h] += 1
            if freq[h] == 2:
                ret.append(s[i:i+10])

        return ret
        
