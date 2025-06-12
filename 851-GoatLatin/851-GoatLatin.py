# Last updated: 12/6/2025, 5:46:16 am
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        n = len(sentence)
        ret = ""
        word = ''

        def helper(word):
            nonlocal ret, cnt
            if word[0].lower() in vowels:
                for w in word:
                    ret += w
                ret += 'ma'
            else:
                for j in range(1, len(word)):
                    ret += word[j]
                ret += word[0] + 'ma'
            ret += 'a' * (cnt+1)
        cnt = 0
        for i in range(n):
            if sentence[i] == ' ':
                helper(word)
                ret += ' '
                word = ''
                cnt += 1
            else:
                word += sentence[i]
        
        helper(word)
        return ret