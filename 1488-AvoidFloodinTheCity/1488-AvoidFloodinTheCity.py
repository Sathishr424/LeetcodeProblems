# Last updated: 7/10/2025, 5:55:32 am
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        nearest = defaultdict(list)
        for i in range(n-1, -1, -1):
            nearest[rains[i]].append(i)
        
        ans = [1] * n
        floods = {}
        heap = []
        for i in range(n):
            lake = rains[i]
            nearest[lake].pop()
            if lake > 0:
                if lake in floods: return []
                floods[lake] = i
                if nearest[lake]:
                    heapq.heappush(heap, (nearest[lake][-1], lake))
                ans[i] = -1
            else:
                while heap and heap[0][0] < i:
                    heapq.heappop(heap)
                
                if heap:
                    _, lake_dry = heapq.heappop(heap)
                    del floods[lake_dry]
                    ans[i] = lake_dry
        
        return ans
