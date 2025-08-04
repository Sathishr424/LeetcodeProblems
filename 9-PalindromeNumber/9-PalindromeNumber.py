# Last updated: 4/8/2025, 11:25:22 pm
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ret = []
        def rec(index, rem, arr):
            if rem == 0:
                ret.append(arr[:])
                return
            
            for i in range(index, n):
                if candidates[i] > rem: break
                arr.append(candidates[i])
                rec(i, rem - candidates[i], arr)
                arr.pop()
        
        rec(0, target, [])
        return ret