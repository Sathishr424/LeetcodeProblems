# Last updated: 5/11/2025, 10:29:49 pm
class MedianFinder:
    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min, num)
        
        if self.min and self.max and -self.max[0] > self.min[0]:
            num = -heapq.heappop(self.max)
            heapq.heappush(self.min, num)
        
        while len(self.min) > len(self.max):
            num = heapq.heappop(self.min)
            heapq.heappush(self.max, -num)

    def findMedian(self) -> float:
        if len(self.min) != len(self.max):
            return -self.max[0]
        return (self.min[0] - self.max[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()