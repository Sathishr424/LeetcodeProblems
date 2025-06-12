# Last updated: 12/6/2025, 5:46:39 am
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dis = [float('inf')] * n
        k += 1
        prev = dis + []
        prev[src] = 0

        for i in range(k):
            change = False
            for x, y, w in flights:
                curr = prev[x] + w
                if curr < dis[y]:
                    dis[y] = curr
                    change = True
            prev = dis + []
            if not change: break
        
        return dis[dst] if dis[dst] != float('inf') else -1