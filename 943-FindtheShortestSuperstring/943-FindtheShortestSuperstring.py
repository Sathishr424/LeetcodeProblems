# Last updated: 5/5/2025, 5:44:31 pm
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
        start_mask = 1 << n
        full_mask = (1 << (n+1)) - 1

        dp = {}
        
        for i in range(n):
            key = f'{start_mask | (1 << i)},{words[i]}'
            dp[key] = words[i]
        
        for i in range(n-1):
            new_dp = {}
            for mask in dp:
                st = dp[mask]
                mask = int(mask.split(',')[0])

                for k in range(n):
                    if mask & (1 << k) == 0:
                        
                        new_mask = mask | (1 << k)
                        new_merge = overlap_append(st, words[k])

                        key = f'{new_mask},{words[k]}'
                        if key not in new_dp or len(new_merge) < len(new_dp[key]):
                            new_dp[key] = new_merge
            
            dp = new_dp
            # print([[format(m, f'0{n+1}b'), s] for m, s in dp])
        ret = d
        for mask in dp:
            if len(dp[mask]) < len(ret):
                ret = dp[mask]
        # print([[format(m, f'0{n+1}b'), s] for m, s in dp])
        # print(ret)
        return ret