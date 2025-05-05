# Last updated: 5/5/2025, 6:13:45 pm
def overlap_append(a: str, b: str) -> str:
    m = len(a)
    n = len(b)

    for i in range(max(0, m-n), m):
        start = i
        for j in range(0, m-i):
            if a[start] != b[j]:
                break
            start += 1
        
        if start == m: return b[j+1:]
        
    return b 
        
d = 'z' * 241

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        start_mask = 1 << n
        full_mask = (1 << (n+1)) - 1

        overlaps = [[''] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j: continue
                overlaps[i][j] = overlap_append(words[i], words[j])

        dp = {}
        
        for i in range(n):
            key = f'{start_mask | (1 << i)},{words[i]}'
            dp[key] = [start_mask | (1 << i), words[i], i]
        
        for i in range(n-1):
            new_dp = {}
            for key in dp:
                mask, st, index = dp[key]

                for k in range(n):
                    if mask & (1 << k) == 0:
                        
                        new_mask = mask | (1 << k)
                        new_merge = st + overlaps[index][k]

                        key = f'{new_mask},{words[k]}'
                        if key not in new_dp or len(new_merge) < len(new_dp[key][1]):
                            new_dp[key] = [new_mask, new_merge, k]
            
            dp = new_dp

        ret = d
        for mask in dp:
            if len(dp[mask][1]) < len(ret):
                ret = dp[mask][1]

        return ret