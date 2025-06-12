# Last updated: 12/6/2025, 5:34:33 am
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        heap = []

        for i in range(m):
            curr = []
            for j in range(n):
                heapq.heappush(curr, grid[i][j])
                if len(curr) > limits[i]:
                    heapq.heappop(curr)
            
            for num in curr:
                heapq.heappush(heap, num)
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return sum(heap)