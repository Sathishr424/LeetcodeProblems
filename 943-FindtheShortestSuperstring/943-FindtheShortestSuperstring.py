# Last updated: 5/5/2025, 4:24:54 pm
def getAlp(a):
    return ord(a) - 96

base = 27
mod = 10**9 + 7

base_powers = [1] * (20 + 1)
for i in range(1, 20 + 1):
    base_powers[i] = base_powers[i - 1] * base % mod

def overlap_append_rolling_hash(st, s):
    max_len = min(len(st), len(s))

    match_ = 0
    hash_st = 0
    hash_s = 0

    for i in range(1, max_len + 1):
        hash_st = (getAlp(st[-i]) * base_powers[i - 1] + hash_st) % mod
        hash_s = (hash_s * base + getAlp(s[i - 1])) % mod
        if hash_st == hash_s:
            match_ = i

    return st + s[match_:]

def overlap_append(a: str, b: str) -> str:
    m = len(a)
    n = len(b)

    for i in range(max(0, m-n), m):
        start = i
        for j in range(0, m-i):
            if a[start] != b[j]:
                break
            start += 1
        
        if start == m: return a[:i] + b
        
    return a + b 

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # words = test_words
        n = len(words)
        
        d = 'z'
        for word in words:
            d += 'z' * len(word)
        
        full_mask = (1 << (n+1)) - 1
        start_mask = 1 << n

        memo = {}
        ret = d

        def rec(mask, st):
            if mask == full_mask: return st
            
            key = f"{mask},{st}"
            if key in memo: return memo[key]

            ans = d
            for i in range(n):
                if mask & (1 << i) == 0:
                    curr = rec(mask | (1 << i), words[i])
                    merged = overlap_append(st, curr)
                    if len(merged) < len(ans):
                        ans = merged
            memo[key] = ans
            return ans

        return rec(start_mask, '')