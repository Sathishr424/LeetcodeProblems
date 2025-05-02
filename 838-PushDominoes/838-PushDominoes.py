# Last updated: 2/5/2025, 4:30:21 pm
class Solution:
    def pushDominoes(self, dom: str) -> str:
        n = len(dom)
        dom = list(dom)

        dp = [float('inf')] * n
        f = -float('inf')
        for i in range(n):
            if dom[i] == 'R':
                f = 1
            elif dom[i] == 'L':
                f = -1
            else:
                if f > 0:
                    f += 1
                else:
                    f = -float('inf')
            
            dp[i] = f
        f = float('inf')
        for i in range(n-1, -1, -1):
            if dom[i] == 'L':
                f = -1
            elif dom[i] == 'R':
                f = 1
            else:
                if f < 0:
                    f -= 1
                else:
                    f = float('inf')

                if abs(f) < abs(dp[i]):
                    dom[i] = 'L'
                elif abs(f) > abs(dp[i]):
                    dom[i] = 'R'
        
        return ''.join(dom)
        
