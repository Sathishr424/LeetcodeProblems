# Last updated: 9/18/2026, 10:34:55 AM
1class Solution:
2    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
3        prices.sort()
4        discounts.sort()
5
6        ans = 0
7        while prices and discounts:
8            price = prices.pop()
9            discount = discounts.pop()
10
11            ans += price - (price * (discount / 100))
12
13        while prices:
14            ans += prices.pop()
15
16        return ans