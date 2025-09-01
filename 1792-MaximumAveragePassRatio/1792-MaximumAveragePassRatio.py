# Last updated: 1/9/2025, 10:33:56 pm
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)

        heap = []
        students = [0] * n
        total = [0] * n

        for i in range(n):
            students[i] = classes[i][0]
            total[i] = classes[i][1]

        for i, (p, t) in enumerate(classes):
            if p == t: continue
            heapq.heappush(heap, ((p / t - (p + 1) / (t + 1)), p, t, i))

        while extraStudents and heap:
            diff, p, t, index = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, ((p / t - (p + 1) / (t + 1)), p, t, index))
            extraStudents -= 1
        
        for _, p, t, index in heap:
            students[index] = p
            total[index] = t

        s = 0
        for i in range(n):
            s += students[i] / total[i]

        return s / n