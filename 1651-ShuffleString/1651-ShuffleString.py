# Last updated: 12/6/2025, 5:41:06 am
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return self.bubbleSort(list(s),indices)
    
    def bubbleSort(self, s, ind):
        change = False
        for i in range(len(ind)-1):
            if ind[i] > ind[i+1]:
                ind[i], ind[i+1] = ind[i+1], ind[i]
                s[i],s[i+1] = s[i+1],s[i]
                change = True
        if not change: return ''.join(s)
        return self.bubbleSort(s, ind)