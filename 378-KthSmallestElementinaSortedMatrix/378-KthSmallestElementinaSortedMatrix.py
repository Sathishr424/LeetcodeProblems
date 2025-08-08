# Last updated: 9/8/2025, 2:39:04 am
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def minHeap():
            heap = []

            for i in range(min(n, k)):
                heapq.heappush(heap, (matrix[i][0], i, 0))

            for _ in range(k-1):
                num, i, j = heapq.heappop(heap)
                if j + 1 < n:
                    heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            
            return heap[0][0]
        
        def maxHeap():
            heap = []

            for i in range(n-1, max(-1, n-k-1), -1):
                heapq.heappush(heap, (-matrix[i][n-1], i, n-1))
            
            for _ in range(k - 1):
                _, i, j = heapq.heappop(heap)
                print(i, j)
                if j - 1 >= 0:
                    heapq.heappush(heap, (-matrix[i][j-1], i, j-1))
            
            return -heapq.heappop(heap)[0]

        m_k = (n * n) - k + 1
        if m_k < k:
            k = m_k
            return maxHeap()
        return minHeap()