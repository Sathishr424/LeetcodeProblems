# Last updated: 12/6/2025, 5:37:56 am
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        tmp = {'M': 0, "G": 1, 'P': 2}
        ans = [0, 0, 0]

        for i in range(len(garbage)-1, -1, -1):
            s = garbage[i]
            for j in s:
                ans[tmp[j]] += 1
            if i > 0:
                for k in range(3):
                    if ans[k]: ans[k] += travel[i-1]
        
        return sum(ans)