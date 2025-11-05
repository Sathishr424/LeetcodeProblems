# Last updated: 5/11/2025, 10:42:51 pm
class MedianFinder:
    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        if len(self.min) == 0:
            heapq.heappush(self.max, -num)
        elif num > self.min[0]:
            heapq.heappush(self.min, num)
        else:
            heapq.heappush(self.max, -num)
        
        while len(self.min) > len(self.max):
            num = heapq.heappop(self.min)
            heapq.heappush(self.max, -num)
        
        while len(self.max) > len(self.min) + 1:
            num = -heapq.heappop(self.max)
            heapq.heappush(self.min, num)
        
        # print(self.max, self.min)

    def findMedian(self) -> float:
        if len(self.min) != len(self.max):
            return -self.max[0]
        return (self.min[0] - self.max[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()