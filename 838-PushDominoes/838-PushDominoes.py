# Last updated: 2/5/2025, 4:37:14 pm
inf = 10**5 + 1
class Solution:
    def pushDominoes(self, dom: str) -> str:
        n = len(dom)
        dom = list(dom)

        dp = [inf] * n
        f = inf

        for i in range(n):
            if dom[i] == 'R':
                f = 1
            elif dom[i] == 'L':
                f = inf
            else:
                f = min(inf, f + 1)
            
            dp[i] = f
        
        f = inf
        
        for i in range(n-1, -1, -1):
            if dom[i] == 'L': 
                f = 1
            elif dom[i] == 'R':
                f = inf
            else: 
                f = min(inf, f + 1)
                
                if f < dp[i]:
                    dom[i] = 'L'
                elif f > dp[i]:
                    dom[i] = 'R'
        
        return ''.join(dom)
        
