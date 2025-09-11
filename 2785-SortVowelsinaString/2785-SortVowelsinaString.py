# Last updated: 11/9/2025, 2:46:41 pm
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        for char in s:
            if char.lower() in 'aeiou':
                vowels.append(char)
        
        vowels.sort(key=lambda x: -ord(x))

        ret = []
        for char in s:
            if char.lower() in 'aeiou':
                ret.append(vowels.pop())
            else:
                ret.append(char)
        
        return ''.join(ret)
