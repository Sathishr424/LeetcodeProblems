# Last updated: 7/7/2025, 7:00:40 pm
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        canVisit = 0

        heap = []
        events.sort()
        end = max([e for _, e in events])
        index = 0
        for day in range(0, end + 1):
            while index < n and events[index][0] <= day:
                heapq.heappush(heap, events[index][1])
                index += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                canVisit += 1
                heapq.heappop(heap)
        
        return canVisit