# Last updated: 11/23/2026, 3:39:23 PM
1class ProductOfNumbers:
2    def __init__(self):
3        self.zeros = [0]
4        self.prefix = [1]
5
6    def add(self, num: int) -> None:
7        if num == 0: self.zeros.append(len(self.prefix))
8        num = max(num, 1)
9        self.prefix.append(self.prefix[-1] * num)
10        # print(self.prefix, self.zeros)
11
12    def getProduct(self, k: int) -> int:
13        n = len(self.prefix)
14        left = n - k
15        index = bisect_left(self.zeros, n - k)
16        # print(k, (n, left, index), self.prefix, self.zeros)
17        if index < len(self.zeros) and self.zeros[index] >= left: return 0
18        return self.prefix[-1] // self.prefix[-k-1]
19
20
21# Your ProductOfNumbers object will be instantiated and called as such:
22# obj = ProductOfNumbers()
23# obj.add(num)
24# param_2 = obj.getProduct(k)