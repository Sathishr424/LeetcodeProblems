# Last updated: 12/6/2025, 5:54:38 am
class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        n = len(cand)
        cand.sort()
        ret = []
        arr = []
    
        def dfs(index, tot):
            if tot == target:
                return ret.append(arr[:])
            
            for i in range(index, n):
                if tot + cand[i] > target: break
                if i > index and cand[i] == cand[i-1]: continue
                arr.append(cand[i])
                dfs(i+1, tot+cand[i])
                arr.pop()
        
        dfs(0, 0)
        return ret
