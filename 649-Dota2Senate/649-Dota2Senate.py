# Last updated: 12/6/2025, 5:47:53 am
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_stack = deque([])
        d_stack = deque([])

        for i, s in enumerate(senate):
            if s == 'D':
                d_stack.append(i)
            else:
                r_stack.append(i)
        
        n = len(senate)
    
        while r_stack and d_stack:
            if r_stack[0] < d_stack[0]:
                s = 'R'
                index = r_stack.popleft()
            else:
                s = 'D'
                index = d_stack.popleft()
            
            if s == 'R':
                if d_stack: d_stack.popleft()
                r_stack.append(index + n)
            else:
                if r_stack: r_stack.popleft()
                d_stack.append(index + n)
        
        return 'Radiant' if r_stack else 'Dire'
            
