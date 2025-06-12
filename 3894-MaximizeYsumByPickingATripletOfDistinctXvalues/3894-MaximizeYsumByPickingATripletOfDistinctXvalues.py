# Last updated: 12/6/2025, 5:33:13 am
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)

        heap = []
        for i, num in enumerate(y):
            heapq.heappush(heap, (-num, i))

        a = heapq.heappop(heap)[1]

        while heap and x[heap[0][1]] == x[a]:
            heapq.heappop(heap)
        
        if not heap: return -1
            
        b = heapq.heappop(heap)[1]
        
        while heap and (x[heap[0][1]] == x[a] or x[heap[0][1]] == x[b]):
            heapq.heappop(heap)

        if not heap: return -1
        
        c = heapq.heappop(heap)[1]

        return y[a] + y[b] + y[c]
        
            