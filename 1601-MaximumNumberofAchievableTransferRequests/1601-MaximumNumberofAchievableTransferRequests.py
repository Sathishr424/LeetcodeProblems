# Last updated: 30/7/2025, 4:57:08 pm
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)

        best = 0
        for mask in range((1 << m)-1, 0, -1):
            cnt = bin(mask).count('1')
            if cnt <= best: continue

            buildings = [0] * n
            for i in range(m):
                if mask & (1 << i):
                    buildings[requests[i][1]] += 1
                    buildings[requests[i][0]] -= 1
            
            fine = True
            for b in buildings:
                if b != 0:
                    fine = False
                    break
            
            if fine: best = cnt

        return best