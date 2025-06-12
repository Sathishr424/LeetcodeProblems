# Last updated: 12/6/2025, 5:50:18 am
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = []
        vow = {'A': 1, 'a': 1, 'e': 1, 'E': 1, 'I': 1, 'i': 1, 'o': 1, 'O': 1, 'u': 1, 'U': 1}
        for w in s:
            if w in vow:
                 arr.append(w)

        ret = ""
        for w in s:
            if w in vow:
                ret += arr.pop()
            else:
                ret += w
        
        return ret
