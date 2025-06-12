# Last updated: 12/6/2025, 5:43:19 am
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        alp = [0] * 26
        for a in brokenLetters:
            alp[ord(a)-97] = 1
        
        ans = 0
        word = ""
        cant = False
        for char in text:
            if char == ' ':
                if not cant: ans += 1
                else: cant = False
                word = ""
            elif cant: continue
            elif alp[ord(char)-97]:
                cant = True
            else:
                word += char
        
        if not cant: ans += 1
        return ans