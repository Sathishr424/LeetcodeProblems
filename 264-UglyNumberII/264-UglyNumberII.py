# Last updated: 21/6/2025, 2:34:52 pm
ugly = []
index = 1
heap = [1]
there = {}
num = 1
while index < 1691:
    num = heapq.heappop(heap)
    if num in there: continue
    ugly.append(num)
    there[num] = 1
    index += 1
    heapq.heappush(heap, num * 2)
    heapq.heappush(heap, num * 3)
    heapq.heappush(heap, num * 5)
ugly.append(num)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return ugly[n-1]