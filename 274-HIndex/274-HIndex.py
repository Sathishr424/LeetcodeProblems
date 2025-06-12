# Last updated: 12/6/2025, 5:50:58 am
class Solution:
    def hIndex(self, cit: List[int]) -> int:
        cit.sort(reverse=True)
        n = len(cit)
        for i in range(n):
            if i+1 == cit[i]: return cit[i]
            elif i+1 > cit[i]: return i
        return n