# Last updated: 12/6/2025, 5:40:11 am
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1: return [1]
        m = n*2-1
        arr = [0 for _ in range(m)]

        arr[0] = n
        arr[n] = n

        balances = [i for i in range(n-1, 1, -1)]

        def rec(index, vis):
            nonlocal balances
            if index == m:  return True
            if arr[index] != 0: return rec(index+1, vis)
            def helper(b):
                if index+b < m and arr[index+b] == 0:
                    vis[b] = 1
                    arr[index] = b
                    arr[index+b] = b
                    if rec(index+1, vis): return True
                    del vis[b]
                    arr[index] = 0
                    arr[index+b] = 0
                return False
            
            for b in balances:
                if b not in vis and helper(b): return True

            if 1 not in vis:
                vis[1] = 1
                arr[index] = 1
                if rec(index+1, vis): return True
                del vis[1]
                arr[index] = 0
            return False
        
        found = rec(1, {n: 1})
        if found: return arr
        return []