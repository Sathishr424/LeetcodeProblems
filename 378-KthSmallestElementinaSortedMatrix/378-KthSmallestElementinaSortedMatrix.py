# Last updated: 8/8/2025, 2:33:11 am
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        heap = []

        for i in range(min(n, k)):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        for _ in range(k-1):
            num, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        
        return heap[0][0]