# Last updated: 7/10/2025, 5:57:23 am
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        nearest = defaultdict(list)
        for i in range(n-1, -1, -1):
            nearest[rains[i]].append(i)
        
        ans = [1] * n
        floods = set()
        heap = []
        for i in range(n):
            lake = rains[i]
            nearest[lake].pop()
            if lake > 0:
                if lake in floods: return []
                floods.add(lake)
                if nearest[lake]:
                    heapq.heappush(heap, (nearest[lake][-1], lake))
                ans[i] = -1
            else:
                while heap and heap[0][0] < i:
                    heapq.heappop(heap)
                
                if heap:
                    _, lake_dry = heapq.heappop(heap)
                    floods.remove(lake_dry)
                    ans[i] = lake_dry
        
        return ans
