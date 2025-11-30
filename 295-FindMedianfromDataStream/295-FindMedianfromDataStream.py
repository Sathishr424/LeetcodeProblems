# Last updated: 1/12/2025, 1:38:28 am
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
11        while self.left and self.right and -self.left[0] > self.right[0]:
12            heapq.heappush(self.right, -heapq.heappop(self.left))
13
14        half = ceil(self.n / 2)
15
16        while len(self.left) > half:
17            heapq.heappush(self.right, -heapq.heappop(self.left))
18        
19        while len(self.right) > self.n // 2:
20            heapq.heappush(self.left, -heapq.heappop(self.right))
21
22
23    def findMedian(self) -> float:
24        # print(self.n, self.left, self.right)
25        if self.n % 2:
26            return -self.left[0]
27        else:
28            return (-1 * self.left[0] + self.right[0]) / 2  
29
30
31# Your MedianFinder object will be instantiated and called as such:
32# obj = MedianFinder()
33# obj.addNum(num)
34# param_2 = obj.findMedian()