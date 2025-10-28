# Last updated: 28/10/2025, 6:10:57 pm
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)

        heap = []
        for g in gifts:
            heapq.heappush(heap, -g)

        while k:
            g = -heapq.heappop(heap)
            heapq.heappush(heap, -(floor(sqrt(g))))
            k -= 1

        return -sum(heap)
            