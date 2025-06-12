# Last updated: 12/6/2025, 5:36:39 am

class Solution:
    def sortVowels(self, s: str) -> str:
        vow = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'a': 0, 'e': 0, "i": 0, 'o': 0, 'u': 9}
        arr = []
        for w in s:
            if w in vow:
                arr.append(w)
        arr.sort(reverse=True)
        ret = ""
        index = 0
        for w in s:
            if w in vow:
                ret += arr.pop()
            else: 
                ret += w

        return ret