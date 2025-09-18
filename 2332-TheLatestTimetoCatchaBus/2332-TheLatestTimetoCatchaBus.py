# Last updated: 18/9/2025, 10:52:15 am
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        available = []
        
        if buses[0] not in passengers:
            available.append(buses[0])
        prev = 0
        
        for p in passengers:
            if p-1 != prev:
                available.append(p - 1)
            prev = p
        
        if buses[-1] not in passengers:
            available.append(buses[-1])

        available.sort()

        def isGood(new_p):
            heap = []
            for p in passengers:
                heapq.heappush(heap, p)
            
            heapq.heappush(heap, new_p)
    
            for bus in buses:
                rem = capacity
    
                while rem and heap and heap[0] <= bus:
                    p = heapq.heappop(heap)
                    if p == new_p: return True
                    rem -= 1
            
            return False
        
        l = 0
        r = len(available) - 1

        while l < r:
            mid = (l + r + 1) // 2

            if isGood(available[mid]):
                l = mid
            else:
                r = mid - 1

        return available[l]
        
            