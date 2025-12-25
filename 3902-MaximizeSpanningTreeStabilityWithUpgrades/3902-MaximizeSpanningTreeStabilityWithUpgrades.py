# Last updated: 12/25/2025, 7:11:00 PM
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return True

        if self.sizes[y] > self.sizes[x]:
            x, y = y, x

        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        return False

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        union = Union(n)

        new_arr = []
        score = inf
        for x, y, s, must in edges:
            if must == 1:
                if union.union(x, y): return -1
                score = min(score, s)
            else:
                new_arr.append((x, y, s))

        new_arr.sort(reverse=True, key=lambda x: x[2])
        # print(new_arr, score)
        heap = []
        scores = []
        for i, (x, y, s) in enumerate(new_arr):
            if union.union(x, y): continue
            scores.append((s, i))
            heapq.heappush(heap, (-s, i))
            if len(heap) > k:
                heapq.heappop(heap)

        to_delete = {}
        while heap:
            _, i = heapq.heappop(heap)
            to_delete[i] = 1
            score = min(score, new_arr[i][2] * 2)

        for s, i in scores:
            if i in to_delete: continue
            score = min(score, s)

        for i in range(1, n):
            if union.find(i) != union.find(i - 1): return -1
        return score
                