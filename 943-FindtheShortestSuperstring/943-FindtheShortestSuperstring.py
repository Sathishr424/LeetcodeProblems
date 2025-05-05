# Last updated: 5/5/2025, 4:48:17 pm
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

        
d = 'z' * 241

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        memo = {}

        def rec(mask, st):
            if mask == 0: return st
            
            key = f"{mask},{st}"
            if key in memo: return memo[key]

            ans = d
            for i in range(n):
                if (mask >> i) & 1:
                    curr = rec(mask & ~(1 << i), words[i])
                    merged = overlap_append(st, curr)
                    if len(merged) < len(ans):
                        ans = merged
            memo[key] = ans
            return ans

        return rec((1 << n) - 1, '')