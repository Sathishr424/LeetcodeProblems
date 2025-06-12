# Last updated: 12/6/2025, 5:51:48 am
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(t)
        hash_s = {}
        hash_t = {}
        for i in range(n):
            if s[i] not in hash_s:
                if t[i] in hash_t: return False
                hash_s[s[i]] = t[i]
                hash_t[t[i]] = 1
            elif hash_s[s[i]] != t[i]:
                return False

        return True