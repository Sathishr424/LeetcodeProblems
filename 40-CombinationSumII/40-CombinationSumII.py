# Last updated: 4/8/2025, 11:34:43 pm
class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        n = len(cand)
        cand.sort()
        ret = []
        print(cand)

        def rec(index, rem, arr):
            if rem == 0:
                ret.append(arr[:])
                return
            if index == n: return
            
            for i in range(index, n):
                if cand[i] > rem: break
                if i > index and cand[i] == cand[i - 1]: continue
                arr.append(cand[i])
                rec(i + 1, rem - cand[i], arr)
                arr.pop()
        
        rec(0, target, [])
        return ret