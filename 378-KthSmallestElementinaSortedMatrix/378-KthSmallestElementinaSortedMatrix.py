# Last updated: 8/8/2025, 2:07:33 am
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        heap = []

        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return -heap[0]