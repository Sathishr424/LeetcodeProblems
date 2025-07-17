# Last updated: 17/7/2025, 9:13:56 pm
cmax = lambda x, y: x if x > y else y
mod = 10**9 + 7
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sorted_eff = []
        for i in range(n):
            sorted_eff.append((efficiency[i], i))
        
        sorted_eff.sort(key=lambda x: -x[0])

        heap = []
        s = 0
        performance = 0

        for i in range(n):
            eff, index = sorted_eff[i]       
            heapq.heappush(heap, speed[index])
            s += speed[index]

            if len(heap) > k:
                s -= heapq.heappop(heap)

            performance = cmax(performance, (s * eff))
            
        return performance % mod