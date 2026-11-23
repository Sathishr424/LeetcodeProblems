# Last updated: 11/23/2026, 3:47:02 PM
1class ProductOfNumbers:
2    def __init__(self):
3        self.last_zero = 0
4        self.prefix = [1]
5
6    def add(self, num: int) -> None:
7        if num == 0: 
8            self.last_zero = len(self.prefix)
9            self.prefix.append(1)
10        else:
11            self.prefix.append(self.prefix[-1] * num)
12
13    def getProduct(self, k: int) -> int:
14        n = len(self.prefix)
15        left = n - k
16        if self.last_zero >= left: return 0
17        return self.prefix[-1] // self.prefix[left - 1]
18
19# Your ProductOfNumbers object will be instantiated and called as such:
20# obj = ProductOfNumbers()
21# obj.add(num)
22# param_2 = obj.getProduct(k)