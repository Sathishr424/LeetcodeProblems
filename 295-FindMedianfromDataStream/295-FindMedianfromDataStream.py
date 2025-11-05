# Last updated: 5/11/2025, 10:43:23 pm
class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.right) == 0:
            heapq.heappush(self.left, -num)
        elif num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        while len(self.right) > len(self.left):
            num = heapq.heappop(self.right)
            heapq.heappush(self.left, -num)
        
        while len(self.left) > len(self.right) + 1:
            num = -heapq.heappop(self.left)
            heapq.heappush(self.right, num)

    def findMedian(self) -> float:
        if len(self.right) != len(self.left):
            return -self.left[0]
        return (self.right[0] - self.left[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()