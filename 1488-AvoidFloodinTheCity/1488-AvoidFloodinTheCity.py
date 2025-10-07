# Last updated: 7/10/2025, 5:57:04 am
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        nearest = defaultdict(list)
        for i in range(n):
            nearest[rains[i]].append(i)
        
        ans = [1] * n
        floods = set()
        heap = []
        for i in range(n):
            lake = rains[i]
            if lake > 0:
                if lake in floods: return []
                floods.add(lake)
                index = bisect_left(nearest[lake], i + 1)
                if index != len(nearest[lake]):
                    heapq.heappush(heap, (nearest[lake][index], lake))
                ans[i] = -1
            else:
                while heap and heap[0][0] < i:
                    heapq.heappop(heap)
                
                if heap:
                    _, lake_dry = heapq.heappop(heap)
                    floods.remove(lake_dry)
                    ans[i] = lake_dry
        
        return ans
