# Last updated: 18/7/2025, 10:10:02 pm
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2: return False
        
        openB = []
        unlocked = []

        for i in range(n):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                openB.append(i)
            else:
                if openB: openB.pop()
                elif unlocked: unlocked.pop()
                else: return False
        
        while openB and unlocked and openB[-1] < unlocked[-1]:
            openB.pop()
            unlocked.pop()
        
        return len(openB) == 0
