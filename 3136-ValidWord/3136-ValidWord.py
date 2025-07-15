# Last updated: 15/7/2025, 9:22:49 am
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False

        vow = 0
        cons = 0
        for char in word.lower():
            if char in 'aeiou':
                vow += 1
            elif ord(char) >= ord('a') and ord(char) <= ord('z'):
                cons += 1
            elif ord(char) >= ord('0') and ord(char) <= ord('9'):
                pass
            else:
                return False
        
        return vow > 0 and cons > 0