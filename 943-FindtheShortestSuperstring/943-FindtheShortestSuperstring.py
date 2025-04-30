# Last updated: 1/5/2025, 4:20:33 am
def getAlp(a):
    return ord(a) - 96

test_words = []
for i in range(12):
    word = ''
    for j in range(20):
        word += chr(random.randrange(0, 26) + 97)
    test_words.append(word)

base = 27
mod = 10**9 + 7

def getSt(st, s):
    right = 0
    left = 0

    l = len(st)-1
    r = 0

    match_ = 0

    for i in range(min(len(st), len(s))):
        left = (left + (pow(base, r, mod) * getAlp(st[l]) % mod)) % mod
        right = ((right * base % mod) + getAlp(s[r])) % mod
        if left == right:
            match_ = r+1
        l -= 1
        r += 1
    return st + s[match_:]

def compare(x, y):
    if len(x) < len(y): return x
    return y

def overlap_append(a: str, b: str) -> str:
    for i in range(max(1, len(a) - len(b)), len(a)):
        match = True
        for j in range(i, len(a)):
            if a[j] != b[j - i]:
                match = False
                break
        if match:
            return a[:i] + b
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

