# Last updated: 12/9/2025, 9:21:13 am
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        n = len(s)

        vowels = 0
        for char in s:
            if char in 'aeiou':
                vowels += 1
        
        if vowels == 0: return False
        return True