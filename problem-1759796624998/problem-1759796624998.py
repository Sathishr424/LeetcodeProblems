# Last updated: 7/10/2025, 5:53:44 am
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        nearest = defaultdict(list)
        for i in range(n):
            nearest[rains[i]].append(i)
        
        ans = [1] * n
        floods = {}
        heap = []
        for i in range(n):
            lake = rains[i]
            if lake > 0:
                if lake in floods: return []
                floods[lake] = i
                index = bisect_left(nearest[lake], i + 1)
                if index != len(nearest[lake]):
                    heapq.heappush(heap, (nearest[lake][index], lake))
                ans[i] = -1
            else:
                while heap and heap[0][0] < i:
                    heapq.heappop(heap)
                
                if heap:
                    _, lake_dry = heapq.heappop(heap)
                    del floods[lake_dry]
                    ans[i] = lake_dry
        
        return ans
