# Last updated: 12/6/2025, 5:47:11 am
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = [float('inf')] * (n+1)
        dis[0] = 0
        dis[k] = 0

        for i in range(n-1):
            change = False
            for x, y, t in times:
                time = dis[x] + t
                if time < dis[y]:
                    change = True
                    dis[y] = time
            if not change: break
        
        ans = max(dis)
        return ans if ans != float('inf') else -1
            
        
