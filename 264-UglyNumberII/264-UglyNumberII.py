# Last updated: 21/6/2025, 2:30:38 pm

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        index = 1
        heap = [1]
        num = 1
        there = {}
        while index <= n:
            num = heapq.heappop(heap)
            if num in there: continue
            there[num] = 1
            index += 1
            heapq.heappush(heap, num * 2)
            heapq.heappush(heap, num * 3)
            heapq.heappush(heap, num * 5)
        return num