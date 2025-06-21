# Last updated: 21/6/2025, 2:32:00 pm
ugly = []
index = 1
heap = [1]
there = {}
while index <= 1690:
    num = heapq.heappop(heap)
    if num in there: continue
    ugly.append(num)
    there[num] = 1
    index += 1
    heapq.heappush(heap, num * 2)
    heapq.heappush(heap, num * 3)
    heapq.heappush(heap, num * 5)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return ugly[n-1]