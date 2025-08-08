# Last updated: 9/8/2025, 2:34:12 am
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        heap = []
        k = (n * n) - k

        for i in range(n):
            heapq.heappush(heap, (-matrix[i][n-1], i, n-1))
        
        for _ in range(k):
            _, i, j = heapq.heappop(heap)
            if j - 1 >= 0:
                heapq.heappush(heap, (-matrix[i][j-1], i, j-1))
        
        return -heapq.heappop(heap)[0]