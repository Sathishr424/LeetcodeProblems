# Last updated: 9/10/2025, 8:39:16 pm
cmin = lambda x, y: x if x < y else y

class Solution:
    def findCrossingTime(self, n: int, k: int, workers: List[List[int]]) -> int:
        left = []
        right = []
        picked = []
        leftFree = []
        for i, (r, pick, l, put) in enumerate(workers):
            heapq.heappush(leftFree, (-(l + r), -i))

        elapsed = 0
        while n or right or picked:
            while right and right[0][0] <= elapsed:
                t, c, index = heapq.heappop(right)
                heapq.heappush(picked, (c, index))
            while left and left[0][0] <= elapsed:
                t, c, index = heapq.heappop(left)
                heapq.heappush(leftFree, (c, index))
            
            if picked:
                c, index = heapq.heappop(picked)
                r, pick, l, put = workers[-index]
                t = elapsed
                heapq.heappush(left, (t + l + put, c, index))
                elapsed += l
            elif n and leftFree:
                c, index = heapq.heappop(leftFree)
                r, pick, l, put = workers[-index]
                t = elapsed
                heapq.heappush(right, (t + r + pick, c, index))
                elapsed += r
                n -= 1
            elif left and right:
                elapsed = cmin(left[0][0], right[0][0])
            elif left:
                elapsed = left[0][0]
            else:
                elapsed = right[0][0]
                
        return elapsed