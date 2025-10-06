# Last updated: 7/10/2025, 4:54:51 am
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        left = [ord(a) - ord('a') + 1 for a in s1]
        right = [ord(a) - ord('a') + 1 for a in s2]
        evil_arr = [ord(a) - ord('a') + 1 for a in evil]
        # print(left)
        # print(right)
        # print(evil_arr)
        m = len(evil_arr)
        mod = 10 ** 9 + 7

        lcp = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil_arr[j] != evil_arr[i]:
                j = lcp[j - 1]
            
            if evil_arr[j] == evil_arr[i]:
                j += 1
                lcp[i] = j
        # print(lcp, "LCP")
        def getNewMatch(match, val):
            if evil_arr[match] == val:
                return match + 1
            else:
                while match > 0 and evil_arr[match] != val:
                    match = lcp[match - 1]
                if evil_arr[match] == val:
                    return match + 1
                return match
        # aabbaacc
        # 010012
        cached = {}
        def rec(pos, leading, match, strict, s):
            if pos == n:
                return 1 if not leading else 0
            
            key = (pos, leading, match, strict)
            if key in cached: return cached[key]
            ans = 0
            limit = s[pos] if strict else 26
            for i in range(0, limit + 1):
                if not leading and i == 0: continue
                new_leading = leading and i == 0
                new_strict = strict and i == s[pos]
                new_match = getNewMatch(match, i)
                if new_match == m: continue

                ans += rec(pos + 1, new_leading, new_match, new_strict, s)
            ans %= mod
            cached[key] = ans
            return ans
        
        l = rec(0, 1, 0, 1, left)
        # print("Left:", l)
        cached = {}
        r = rec(0, 1, 0, 1, right)
        # print("Right:", r)
        # print(s1.find(evil))
        if s1.find(evil) == -1:
            l = (l - 1) % mod
        
        return (r - l) % mod