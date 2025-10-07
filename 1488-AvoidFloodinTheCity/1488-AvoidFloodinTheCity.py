# Last updated: 7/10/2025, 9:08:33 am
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        
        nearest = defaultdict(list)
        for i in range(n):
            nearest[rains[i]].append(i)

        full = set()
        heap = []
        ans = [1] * n
        for i in range(n):
            lake = rains[i]
            if lake > 0:
                if lake in full: return []
                full.add(lake)
                index = bisect_left(nearest[lake], i + 1)
                if index != len(nearest[lake]):
                    heapq.heappush(heap, (nearest[lake][index], lake))
                ans[i] = -1
            else:
                while heap and heap[0][0] <= i:
                    heapq.heappop(heap)
                
                if heap:
                    _, dry_lake = heapq.heappop(heap)
                    full.remove(dry_lake)
                    ans[i] = dry_lake
        
        return ans