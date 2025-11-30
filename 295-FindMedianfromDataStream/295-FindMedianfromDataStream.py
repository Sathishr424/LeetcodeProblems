# Last updated: 1/12/2025, 1:39:02 am
1class MedianFinder:
2    def __init__(self):
3        self.left = []
4        self.right = []
5        self.n = 0
6
7    def addNum(self, num: int) -> None:
8        self.n += 1
9        heapq.heappush(self.left, -num)
10
11        if self.left and self.right and -self.left[0] > self.right[0]:
12            heapq.heappush(self.right, -heapq.heappop(self.left))
13
14        half = ceil(self.n / 2)
15
16        if len(self.left) > half:
17            heapq.heappush(self.right, -heapq.heappop(self.left))
18        
19        if len(self.right) > self.n // 2:
20            heapq.heappush(self.left, -heapq.heappop(self.right))
21
22    def findMedian(self) -> float:
23        if self.n % 2:
24            return -self.left[0]
25        else:
26            return (-1 * self.left[0] + self.right[0]) / 2  
27
28
29# Your MedianFinder object will be instantiated and called as such:
30# obj = MedianFinder()
31# obj.addNum(num)
32# param_2 = obj.findMedian()