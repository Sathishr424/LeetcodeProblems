# Last updated: 12/6/2025, 5:45:21 am
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = []
        for w in s:
            if ord(w.lower()) >= 97:
                arr.append(w)
        index = len(arr)-1
        ret = ""
        for w in s:
            if ord(w.lower()) >= 97:
                ret += arr[index]
                index -= 1
            else:
                ret += str(w)
        return ret
