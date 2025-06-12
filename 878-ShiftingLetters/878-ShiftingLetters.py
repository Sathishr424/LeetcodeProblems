# Last updated: 12/6/2025, 5:46:00 am
class Solution:
    def shiftingLetters(self, s, shifts):
        ret = list(s)
        cnt = 0
        for i in shifts:
            cnt += i
        for i in range(len(ret)):
            ret[i] = chr(int(int((ord(ret[i]) - 97)+cnt)%26)+97)
            cnt -= shifts[i]
        return ''.join(ret)