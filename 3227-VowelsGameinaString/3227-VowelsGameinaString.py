# Last updated: 12/9/2025, 9:26:04 am
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for char in s:
            if char in 'aeiou':
                return True
        
        return False