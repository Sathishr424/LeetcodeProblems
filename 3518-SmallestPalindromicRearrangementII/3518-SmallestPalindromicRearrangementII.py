# Last updated: 20/4/2025, 1:44:56 am
@cache
def fact(x):
    if x <= 1: return 1
    return fact(x-1) * x

MAX = 10**6
log_fact = [0] * (MAX+1)
for i in range(1, MAX+1): 
    log_fact[i] = log_fact[i-1] + log2(i)

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        uniq = defaultdict(int)
        for char in s:
            uniq[char] += 1
        
        odd = ''
        half = len(s) // 2
        counts = {}

        def getPerm(k, n):
            if n == 0: return ''

            c = sorted(counts.keys())

            f = log_fact[n]
            for char in counts:
                f -= log_fact[counts[char]]
            
            if f >= 32:
                counts[c[0]] -= 1
                if counts[c[0]] == 0: del counts[c[0]]
                return c[0] + getPerm(k, n-1)

            for char in c:
                counts[char] -= 1
                v = sorted(counts.values(), reverse=True)
                f = 1
                for i in range(v[0]+1, n):
                    f *= i
                for ch in v[1:]:
                    f //= fact(ch)

                if f >= k:
                    if counts[char] == 0: del counts[char]
                    return char + getPerm(k, n-1)
                counts[char] += 1
                k -= f
            
            return ''
        
        for char in uniq:
            if uniq[char] % 2:
                odd = char
            if uniq[char] > 1:
                counts[char] = uniq[char] // 2

        st = getPerm(k, half)
        if len(st) != half: return ''
        
        return st + odd + st[::-1]