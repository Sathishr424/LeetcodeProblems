# Last updated: 12/6/2025, 5:51:35 am
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        def rec(index, s, arr):
            if s == 0 and len(arr) == k: 
                return ret.append(arr + [])
            if len(arr) >= k: return
            
            for i in range(index, 10):
                if s - i >= 0:
                    arr.append(i)
                    rec(i+1, s-i, arr)
                    arr.pop()
                else:
                    break
        rec(1, n, [])
        return ret