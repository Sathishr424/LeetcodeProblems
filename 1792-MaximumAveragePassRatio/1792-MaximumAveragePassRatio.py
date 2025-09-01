# Last updated: 1/9/2025, 10:32:56 pm
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        heap = []

        for i, (p, t) in enumerate(classes):
            heapq.heappush(heap, ((p / t - (p + 1) / (t + 1)), p, t, i))

        while extraStudents and heap:
            diff, p, t, index = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, ((p / t - (p + 1) / (t + 1)), p, t, index))
            extraStudents -= 1
        
        s = 0
        while heap:
            diff, p, t, index = heapq.heappop(heap)
            s += p / t

        return s / n