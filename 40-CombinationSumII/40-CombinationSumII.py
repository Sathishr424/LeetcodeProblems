# Last updated: 4/8/2025, 11:45:00 pm
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        def rec(index, arr, rem):
            if len(arr) == k:
                if rem == 0:
                    ret.append(arr[:])
                return
            
            for i in range(index, 10):
                if i > rem: break
                arr.append(i)
                rec(i + 1, arr, rem - i)
                arr.pop()
        
        rec(1, [], n)
        return ret