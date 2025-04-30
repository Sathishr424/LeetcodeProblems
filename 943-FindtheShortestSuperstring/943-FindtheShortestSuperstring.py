# Last updated: 1/5/2025, 4:53:47 am
def getAlp(a):
    return ord(a) - 96

base = 27
mod = 10**9 + 7

base_powers = [1] * (20 + 1)
for i in range(1, 20 + 1):
    base_powers[i] = base_powers[i - 1] * base % mod

def getSt(st, s):
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

    left = max(0, m-n)
    for i in range(left, m):
        match = True
        for j in range(0, m-i):
            if a[i+j] != b[j]:
                match = False
                break
        if match: return a[:i] + b
        
    return a + b
        

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # words = test_words
        n = len(words)
        
        d = 'z'
        for word in words:
            d += 'z' * len(word)

        memo = {}
        
        full_mask = (1 << (n+1)) - 1
        start_mask = 1 << n

        def dfs(mask, st):
            if mask == full_mask:
                return st
            key = f'{st}|{mask}'
            if key in memo: return memo[key]
            ret = d
            for i in range(n):
                if (1 << i) & mask == 0:
                    s = dfs(mask | (1 << i), words[i])
                    # new_st = getSt(st, s)
                    new_st = overlap_append(st, s)
                    if len(new_st) < len(ret):
                        ret = new_st

            memo[key] = ret
            return ret
        
        return dfs(start_mask, '')

