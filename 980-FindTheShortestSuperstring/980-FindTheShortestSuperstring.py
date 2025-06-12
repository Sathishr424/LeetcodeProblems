# Last updated: 12/6/2025, 5:45:06 am
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
            dp[(start_mask | (1 << i), words[i])] = [words[i], i]
        
        for i in range(n-1):
            new_dp = {}
            for key in dp:
                st, index = dp[key]
                mask, _ = key

                for k in range(n):
                    if mask & (1 << k) == 0:
                        
                        new_mask = mask | (1 << k)
                        new_merge = st + overlaps[index][k]

                        if (new_mask, words[k]) not in new_dp or len(new_merge) < len(new_dp[(new_mask, words[k])][0]):
                            new_dp[(new_mask, words[k])] = [new_merge, k]
            
            dp = new_dp

        ret = None
        for mask in dp:
            if ret == None or len(dp[mask][0]) < len(ret):
                ret = dp[mask][0]

        return ret