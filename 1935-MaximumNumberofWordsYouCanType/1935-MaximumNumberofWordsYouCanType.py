# Last updated: 15/9/2025, 4:57:47 pm
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        count = 0

        for word in words:
            for char in word:
                if char in brokenLetters:
                    break
            else:
                count += 1
        
        return count