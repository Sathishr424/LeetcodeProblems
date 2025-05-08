# Last updated: 9/5/2025, 2:31:57 am
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        m = len(grid)

        heap = []

        for i in range(m):
            for num in sorted(grid[i], reverse=True)[:limits[i]]:
                heapq.heappush(heap, -num)
        
        ret = 0
    
        for i in range(k):
            if not heap: break
            ret += -heapq.heappop(heap)
        
        return ret