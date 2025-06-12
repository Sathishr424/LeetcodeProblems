# Last updated: 12/6/2025, 5:50:47 am
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.n = 0

    def addNum(self, num: int) -> None:
        if len(self.left) == 0:
            self.left.append(-num)
        elif num >= -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.left) > len(self.right)+1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 0: return (-self.left[0] + self.right[0]) / 2
        else: return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()