# Last updated: 12/6/2025, 5:48:50 am
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []

        for i in range(len(profits)):
            heapq.heappush(minHeap, (capital[i], -profits[i]))
        
        maxHeap = []

        while minHeap and minHeap[0][0] <= w:
            _, p = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, p)
        
        while maxHeap:
            p = heapq.heappop(maxHeap)
            w += -p
            k -= 1
            if k == 0: break
            while minHeap and minHeap[0][0] <= w:
                _, p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, p)
    
        return w
