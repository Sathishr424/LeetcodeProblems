# Last updated: 9/5/2025, 9:00:41 pm
class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        n = len(cand)
        cand.sort()
        ret = []

        def dfs(index, tot, arr):
            nonlocal ret
            if tot == target:
                ret.append(arr + [])
                return
            
            for i in range(index, n):
                if tot + cand[i] > target: break
                if i-1 >= index and cand[i] == cand[i-1]: continue
                arr.append(cand[i])
                dfs(i+1, tot+cand[i], arr)
                arr.pop()
        
        dfs(0, 0, [])
        return ret
