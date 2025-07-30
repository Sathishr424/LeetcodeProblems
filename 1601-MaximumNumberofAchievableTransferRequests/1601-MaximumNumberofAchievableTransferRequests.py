# Last updated: 30/7/2025, 4:48:13 pm
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)

        @cache
        def rec(index, mask):
            if index == m:
                buildings = [0] * n
                for i in range(m):
                    if mask & (1 << i):
                        buildings[requests[i][1]] += 1
                        buildings[requests[i][0]] -= 1
                
                for b in buildings:
                    if b != 0: return 0
                
                return bin(mask).count('1')
            
            ans = rec(index + 1, mask)
            ans = max(rec(index + 1, mask | (1 << index)), ans)
            return ans

        return rec(0, 0)