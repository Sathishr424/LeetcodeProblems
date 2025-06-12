# Last updated: 12/6/2025, 5:39:38 am
class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(' ')
        ret = [" "] * len(arr)
        for i in arr:
            ret[int(i[-1])-1] = i[:-1]
        return ' '.join(ret)