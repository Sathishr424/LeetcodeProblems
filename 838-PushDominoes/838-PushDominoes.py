# Last updated: 2/5/2025, 4:39:52 pm
class Solution:
    def pushDominoes(self, dom: str) -> str:
        n = len(dom)
        dom = list(dom)
        
        def simulate(l, r):
            leftForce = 0
            rightForce = 0
            if l-1 >= 0:
                leftForce = -1 if dom[l-1] == 'L' else 1
            if r+1 < n:
                rightForce = -1 if dom[r+1] == 'L' else 1
            
            if leftForce <= 0 and rightForce >= 0: return
            elif leftForce > 0 and rightForce < 0:
                while l < r:
                    dom[l] = 'R'
                    dom[r] = 'L'
                    l += 1
                    r -= 1
            else:
                for i in range(l, r+1):
                    dom[i] = 'L' if leftForce + rightForce < 0 else 'R'

        start = -1
        for i in range(n):
            if dom[i] == '.':
                if start == -1: start = i
            else:
                if start != -1:
                    simulate(start, i-1)
                    start = -1
        
        if start != -1: simulate(start, n-1)

        return ''.join(dom)