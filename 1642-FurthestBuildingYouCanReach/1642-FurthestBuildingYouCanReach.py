# Last updated: 17/7/2025, 7:35:56 pm
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        max_need = []
        for i in range(n - 1):
            if heights[i] < heights[i + 1]:
                need = heights[i + 1] - heights[i]
                heapq.heappush(max_need, need)
                if len(max_need) > ladders:
                    bricks -= heapq.heappop(max_need)
                    if bricks < 0: return i
        
        return n-1