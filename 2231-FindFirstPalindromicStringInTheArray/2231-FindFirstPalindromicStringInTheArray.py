# Last updated: 12/6/2025, 5:38:49 am
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word):
            i = 0
            j = len(word)-1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        for word in words:
            if isPalindrome(word): return word
        return ""