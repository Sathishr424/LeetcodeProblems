# Last updated: 12/6/2025, 5:50:50 am
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash = {}
        hash_s = {}
        s = s.split(' ')
        if len(s) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] not in hash:
                if s[i] in hash_s: return False
                hash[pattern[i]] = s[i]
                hash_s[s[i]] = 1
            elif hash[pattern[i]] != s[i]: 
                return False
        return True