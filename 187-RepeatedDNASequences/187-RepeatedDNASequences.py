# Last updated: 12/8/2025, 1:04:00 am
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10: return []
        base = 31
        mod = 10**9 + 7
        mp = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

        freq = defaultdict(int)
        ret = []

        h = 0
        for i in range(10):
            h = h * base % mod
            h = (h + mp[s[i]]) % mod
        
        freq[h] += 1
    
        for i in range(10, n):
            h = h - (mp[s[i-10]] * pow(base, 9, mod) % mod)
            h %= mod

            h = h * base % mod
            h = (h + mp[s[i]]) % mod

            freq[h] += 1
            if freq[h] == 2:
                ret.append(s[i-9:i+1])

        return ret            
